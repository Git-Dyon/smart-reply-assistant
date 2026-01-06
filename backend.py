import json
from ai_engine import generate_ai_response
from prompts import format_reply_prompt

def process_customer_message(user_input):
    prompt_completo = format_reply_prompt(user_input)
    resposta_bruta = generate_ai_response(prompt_completo)
    
    try:
        # Tenta transformar o texto da IA em um dicionário Python
        dados_resposta = json.loads(resposta_bruta)
        return dados_resposta
    except:
        # Fallback caso a IA erre o formato JSON
        return {
            "curta": "Erro ao formatar. Tente novamente ou atualize a página.",
            "detalhada": resposta_bruta,
            "comercial": "Erro ao formatar. Tente novamente ou atualize a página."
        }
    