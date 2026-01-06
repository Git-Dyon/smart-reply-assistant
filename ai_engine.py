import requests
import json

#def generate_ai_response(prompt, model="llama3.2"):
def generate_ai_response(prompt, model="dolphin-llama3"):
    """
    Envia o prompt para o Ollama local e retorna a resposta da IA.
    """
    url = "http://localhost:11434/api/generate"
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.7,  # Mais criatividade/ousadia, quanto maior o valor mais o comportamento se aproxima do aleatório, quanto mais baixo mais conservador sendo no máximo 1.0.
            "top_p": 0.8 # Controla a diversidade da saída, valores mais baixos resultam em respostas mais focadas.
        }
}

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json().get("response", "Erro: Resposta vazia.")
    except Exception as e:
        return f"Erro ao conectar com Ollama: {str(e)}"

