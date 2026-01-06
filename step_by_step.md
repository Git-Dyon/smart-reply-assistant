
# 🚀 Guia de Implementação: Smart Reply Assistant

Este documento contém o passo a passo consolidado para configurar e executar o assistente de resposta inteligente utilizando **Python** e **Llama 3.2** local.

## 🛠️ Passo 1: Preparação do Ambiente

Considerando um ambiente Windows com VS Code, execute os comandos abaixo no terminal:

1. **Criação da pasta e ambiente virtual:**
```powershell
mkdir smart-reply-assistant
cd smart-reply-assistant
python -m venv venv

```


2. **Ativação do Ambiente (PowerShell):**
*Caso ocorra erro de permissão, execute:* Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
*Ative o venv:*
```powershell
.\venv\Scripts\activate

```


3. **Instalação de Recursos e Dependências:**
```powershell
# Instalação do Ollama (caso não tenha)
winget install ollama

# Baixar o modelo Llama 3.2
ollama pull llama3.2

# Instalação das bibliotecas Python necessárias
pip install requests streamlit

```



---

## 🧠 Passo 2: O Motor de IA (`ai_engine.py`)

Crie o arquivo na raiz do projeto (**fora** da pasta venv). Ele é responsável pela comunicação direta com o Ollama.

```python
import requests

def generate_ai_response(prompt, model="llama3.2"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json().get("response", "Erro: Resposta vazia.")
    except Exception as e:
        return f"Erro ao conectar com Ollama: {str(e)}"

```

---

## 📝 Passo 3: Engenharia de Prompt (`prompts.py`)

Neste arquivo, definimos as "regras de negócio" e o formato de saída obrigatório (JSON).

```python
SYSTEM_INSTRUCTION = """
Você é um assistente de atendimento ao cliente profissional.
Sua tarefa é analisar a mensagem do cliente e gerar EXATAMENTE três opções de resposta no formato JSON.

As opções devem ser:
1. "curta": Uma resposta rápida e direta.
2. "detalhada": Uma resposta empática e explicativa.
3. "comercial": Uma resposta focada em conversão ou fidelização.

FORMATO DE RESPOSTA (Siga estritamente):
{
  "curta": "texto",
  "detalhada": "texto",
  "comercial": "texto"
}
"""

def format_reply_prompt(customer_message):
    return f"{SYSTEM_INSTRUCTION}\n\nMensagem do Cliente: {customer_message}\n\nRetorne apenas o JSON:"

```

---

## ⚙️ Passo 4: Lógica de Processamento (`backend.py`)

Responsável por unir o prompt à IA e tratar os dados recebidos.

```python
import json
from ai_engine import generate_ai_response
from prompts import format_reply_prompt

def process_customer_message(user_input):
    prompt_completo = format_reply_prompt(user_input)
    resposta_bruta = generate_ai_response(prompt_completo)
    
    try:
        # Converte a string da IA em dicionário Python
        return json.loads(resposta_bruta)
    except:
        # Fallback de segurança caso o JSON venha mal formatado
        return {
            "curta": "Erro de formatação.",
            "detalhada": resposta_bruta,
            "comercial": "Erro de formatação."
        }

```

---

## 🎨 Passo 5: Interface Visual (`app.py`)

O "rosto" do projeto, construído com Streamlit para exibição em abas.

```python
import streamlit as st
from backend import process_customer_message

st.set_page_config(page_title="Smart Reply Assistant", page_icon="🤖")

st.title("🤖 Smart Reply Assistant")
st.markdown("Interface para geração de respostas inteligentes via IA local.")

customer_input = st.text_area("Mensagem do cliente:", height=150)

if st.button("Gerar Sugestões"):
    if customer_input.strip():
        with st.spinner("O Llama 3.2 está gerando as opções..."):
            opcoes = process_customer_message(customer_input)
            
            tab1, tab2, tab3 = st.tabs(["⚡ Curta", "📝 Detalhada", "💰 Comercial"])
            
            with tab1:
                st.info(opcoes.get("curta"))
            with tab2:
                st.success(opcoes.get("detalhada"))
            with tab3:
                st.warning(opcoes.get("comercial"))
    else:
        st.error("Por favor, digite uma mensagem primeiro.")

```

---

## ▶️ Como Rodar o Projeto

1. Certifique-se de que o **Ollama** está ativo.
2. No terminal do VS Code (com venv ativo), execute:
```powershell
streamlit run app.py

```