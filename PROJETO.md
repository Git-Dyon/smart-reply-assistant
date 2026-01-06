# Documentação de Projeto de Estudo: Smart Reply Assistant

## 1. Visão Geral do Projeto

**Nome do Projeto:** Smart Reply Assistant (Assistente de Resposta Inteligente)


**Baseado em:** Projeto 02 (Workana) - Automação de Escrita com IA.
**Categoria:** Backend Development / Inteligência Artificial / NLP.

### Descrição

Desenvolvimento de uma aplicação backend com interface simplificada que utiliza Inteligência Artificial para gerar sugestões de respostas automáticas para atendimento ao cliente. O sistema recebe uma mensagem de entrada (simulando um cliente no WhatsApp), analisa o contexto e gera três opções de resposta (Curta, Detalhada e Comercial), permitindo ao operador escolher a melhor opção antes de enviar.

O projeto foca na lógica de processamento de linguagem natural e engenharia de prompt, removendo a complexidade burocrática da API oficial do WhatsApp para focar puramente na inteligência do sistema.

---

## 2. Objetivos Educacionais

A principal finalidade deste projeto é solidificar os conhecimentos em integração de sistemas com LLMs (Large Language Models), saindo da teoria para a prática.

**Habilidades Adquiridas ao Final do Projeto:**

* **Engenharia de Prompt (Prompt Engineering):** Aprender a instruir a IA para adotar personas específicas (ex: "Atendente Solícito") e seguir regras de negócio.
* **Consumo de APIs:** Integração prática com APIs de IA (OpenAI ou Ollama Local).
* **Manipulação de Dados (JSON):** Estruturação de dados para envio e recebimento de payloads da IA.
* **Separação de Responsabilidades:** Arquitetura básica de software (Frontend vs Backend vs Lógica de IA).
* **Lógica de Negócio em Python:** Manipulação de strings e tratamento de erros.

---

## 3. Stack Tecnológico

**Linguagens e Frameworks:**

* 
**Python (3.10+):** Linguagem principal do projeto, escolhida pela sua robustez em tarefas de IA e processamento de dados.


* **Streamlit:** Para criar a interface de usuário (Frontend) de forma rápida, permitindo focar 90% do tempo no código Backend.

**Bibliotecas e Ferramentas:**

* **Ollama (Local) ou OpenAI API:** O motor de inteligência artificial. Como você já usou Ollama no NeuroSIEM, ele é recomendado para custo zero.
* **Requests:** Biblioteca Python para fazer as chamadas HTTP para a API da IA.
* **Dotenv:** Para gerenciamento de variáveis de ambiente (segurança de chaves de API).

---

## 4. Estrutura de Arquivos do Projeto

Esta é a organização sugerida para manter o código limpo e profissional:

```text
smart-reply-assistant/
│
├── app.py                # (Frontend) Interface visual feita com Streamlit
├── backend.py            # (Lógica) Conecta o Frontend com a IA
├── ai_engine.py          # (Integração) Onde a chamada para a API (Ollama/OpenAI) acontece
├── prompts.py            # (Inteligência) Arquivo dedicado apenas para os textos de instrução da IA
├── .env                  # Variáveis de ambiente (URLs, Chaves de API)
├── requirements.txt      # Lista de dependências do projeto
└── README.md             # Documentação de como rodar o projeto

```

---

## 5. Roteiro de Desenvolvimento (Passo a Passo)

Para garantir o aprendizado incremental, o projeto deve ser desenvolvido nas seguintes fases:

### Fase 1: O "Olá Mundo" da IA (Backend Puro)

* **Objetivo:** Criar um script simples em `ai_engine.py` que envia um texto para a IA e imprime a resposta no terminal.
* **Desafio:** Garantir que a IA entenda português e responda de forma coerente.

### Fase 2: Estruturação dos Prompts (O "Cérebro")

* **Objetivo:** No arquivo `prompts.py`, criar templates de texto.
* 
**Ação:** Configurar a IA para não apenas "responder", mas classificar a intenção do cliente (ex: Reclamação, Dúvida, Elogio) antes de gerar o texto.



### Fase 3: Conexão com Interface (Streamlit)

* **Objetivo:** Criar o arquivo `app.py`.
* **Funcionalidade:** O usuário digita a mensagem do cliente em uma caixa de texto, clica em "Gerar Respostas", e o sistema exibe as opções na tela.

### Fase 4: Refinamento (Simulação de Negócio)

* **Objetivo:** Adicionar um seletor de "Tom de Voz" (Formal, Informal, Empático).
* 
**Aplicação:** O sistema deve adaptar a resposta gerada com base na escolha do usuário, atendendo ao requisito de "conteúdos personalizados".



---

## 6. Exemplo de Fluxo de Uso (User Story)

1. **Entrada:** O usuário (atendente) cola a mensagem recebida: *"Meu pedido chegou quebrado, quero devolver."*
2. **Processamento:** O backend envia isso para a IA junto com o prompt de sistema: *"Você é um assistente de suporte focado em retenção de clientes..."*
3. **Saída:** O sistema devolve 3 opções:
* *Opção 1 (Empática):* "Sinto muito por isso! Vamos resolver agora mesmo. Pode me enviar uma foto?"
* *Opção 2 (Direta):* "Para devoluções, acesse o link X e preencha o formulário."
* *Opção 3 (Comercial):* "Pedimos desculpas. Gostaria de trocar pelo mesmo produto ou receber um voucher com 10% extra?"
