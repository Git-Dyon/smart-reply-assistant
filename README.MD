# 🤖 Smart Reply Assistant (Local AI)

> Um assistente inteligente de suporte ao cliente que roda 100% offline, garantindo privacidade e agilidade.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![Ollama](https://img.shields.io/badge/AI-Ollama%20(Llama%203.2)-orange)
![Status](https://img.shields.io/badge/Status-Funcional-brightgreen)

## 📖 Sobre o Projeto

O **Smart Reply Assistant** é uma aplicação Fullstack (Backend Python + Frontend Streamlit) desenvolvida para auxiliar equipes de atendimento ao cliente. 

Diferente de chatbots comuns, este sistema utiliza **Inteligência Artificial Generativa Local (Llama 3.2)** para analisar a mensagem do cliente e sugerir **três opções de resposta** com tons diferentes (Curta, Detalhada e Comercial), permitindo que o humano tome a decisão final.

### 🚀 Destaques Técnicos
* **Privacidade Total:** Utiliza o Ollama rodando localmente. Nenhum dado de cliente sai do servidor/computador.
* **Structured Output (JSON):** A IA não retorna apenas texto; ela é forçada via *Prompt Engineering* a retornar um objeto JSON estruturado, garantindo integração perfeita com o código Python.
* **Arquitetura Modular:** Separação clara de responsabilidades entre Motor de IA, Regras de Negócio (Prompts), Backend e Interface.

---

## 🛠️ Pré-requisitos (Instalação)

Se você está começando do zero e tem apenas o VS Code instalado no Windows, siga os passos abaixo para preparar seu computador.

### 1. Instalar Python e Ollama
Abra o seu **PowerShell** (Terminal do Windows) e execute:

```powershell
# 1. Instalar o Ollama (Motor da IA)
winget install ollama

# 2. Baixar o modelo Llama 3.2 (Cérebro da IA)
ollama run llama3.2
# (Após o download, digite /bye para sair do chat e deixar o servidor rodando)

⚙️ Instalação do Projeto
1. Clonar e preparar a pasta
mkdir smart-reply-assistant
cd smart-reply-assistant

2. Criar Ambiente Virtual (Venv)
Isso isola as bibliotecas do projeto para não bagunçar seu Windows.
python -m venv venv
# Ativar o ambiente (Obrigatório toda vez que for mexer no projeto)
.\venv\Scripts\activate
(Se der erro de permissão no PowerShell, rode: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process e tente ativar de novo).

3. Instalar Dependências
Com o (venv) aparecendo no terminal, instale as bibliotecas necessárias:
pip install streamlit requests


📂 Estrutura do Projeto
Certifique-se de que seus arquivos estejam organizados desta forma na pasta raiz:
smart-reply-assistant/
│
├── ai_engine.py      # Conexão HTTP com a API local do Ollama
├── prompts.py        # Engenharia de Prompt e Regras de Comportamento
├── backend.py        # Lógica principal e tratamento de JSON
├── app.py            # Interface visual (Frontend Streamlit)
└── venv/             # Pasta do ambiente virtual (NÃO MEXER)

▶️ Como Executar
1 - Certifique-se de que o Ollama está rodando (o ícone deve aparecer na bandeja do sistema, perto do relógio).
2 - No terminal do VS Code (com o venv ativo), execute: streamlit run app.py
3 - O navegador abrirá automaticamente no endereço http://localhost:8501.

🧠 Detalhes de Implementação
Engenharia de Prompt (prompts.py)
Utilizamos a técnica de Few-Shot Prompting e Output Enforcement, o sistema instrui o modelo Llama 3.2 a ignorar saídas de texto livre e focar estritamente em um formato JSON:
{
  "curta": "Resposta direta...",
  "detalhada": "Resposta empática...",
  "comercial": "Oferta ou cupom..."
}
Tratamento de Erros (backend.py)
O sistema possui resiliência implementada, caso a IA "alucine" e não entregue um JSON válido, o Python captura a exceção (try/except) e exibe uma mensagem de erro amigável, impedindo que a aplicação trave na tela do usuário.


Essa é uma das partes mais valiosas de um repositório para um desenvolvedor **Júnior**, pois mostra que você não apenas sabe construir, mas também sabe **diagnosticar e documentar problemas comuns**.

Aqui está a seção de **Resolução de Problemas** formatada para você adicionar ao final do seu `README.md`. Ela cobre exatamente o que passamos hoje:

---

## 🆘 Resolução de Problemas (Troubleshooting)

Se você encontrar dificuldades ao rodar o projeto, verifique as soluções abaixo:

Para o seu arquivo **README.md**, uma seção de "Solução de Problemas" (ou *Troubleshooting*) é essencial para ajudar outros desenvolvedores (ou você mesmo no futuro) a resolver gargalos comuns rapidamente.

Aqui está a estrutura pronta para copiar e colar:

---

## 🛠️ Solução de Problemas (Troubleshooting)

Se algo não funcionar como esperado, verifique estes pontos comuns:

### 💻 Erros de Terminal e Ambiente

* **Comando `source` não funciona:** * **Por que ocorre?** Você está usando comandos de Linux no PowerShell do Windows.
* **Solução:** Utilize `.\venv\Scripts\activate`.


* **Erro de Permissão (`PSSecurityException`):** * **Por que ocorre?** O Windows bloqueia a execução de scripts por segurança.
* **Solução:** No terminal, execute:
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`.



---

### 📦 Erros de Bibliotecas (Python/Streamlit)

* **Erro: `module 'streamlit' has no attribute 'copy_button'`:** * **Por que ocorre?** A versão do Streamlit dentro do seu `venv` está desatualizada (precisa ser > 1.22).
* **Solução:** Com o ambiente ativo, force a atualização:
`python -m pip install --upgrade streamlit`.



---

### 🧠 Erros de IA e Conexão

* **Falha ao conectar com o Ollama:** * **Por que ocorre?** O servidor do Ollama não está rodando ou o modelo não foi baixado.
* **Solução:** Verifique se o ícone do Ollama está na bandeja do sistema e se você executou `ollama pull llama3.2`.


* **Erro ao formatar JSON (Resposta Estranha):** * **Por que ocorre?** A IA pode ter enviado texto explicativo antes do código.
* **Solução:** Clique em "Gerar Sugestões" novamente. O sistema possui um mecanismo de *fallback* para tratar esses casos.



---


