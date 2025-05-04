import requests
from bs4 import BeautifulSoup
import json
import time

def obter_json_draft5_furia():
    url = "https://draft5.gg/equipe/330-FURIA"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/91.0.4472.124 Safari/537.36"
        )
    }

    try:
        # Realiza a requisição HTTP para obter a página
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        #Aguardando 3 segundos para pagina carregar
        time.sleep(3)

    except requests.RequestException as e:
        return None, f"Erro ao acessar a página: {e}"

    # Utiliza BeautifulSoup para fazer o parsing da página HTML
    soup = BeautifulSoup(response.text, "html.parser")
    script_tag = soup.find("script", {"id": "__NEXT_DATA__"})

    if not script_tag:
        return None, "❌ JSON embutido não encontrado na página."

    try:
        # Tenta converter o conteúdo da tag <script> em um objeto JSON
        json_data = json.loads(script_tag.string)
        return json_data, None
    except json.JSONDecodeError as e:
        return None, f"Erro ao decodificar JSON: {e}"

# Função para acessar os dados específicos do JSON
def acessar_dados(json_dados, chave):
    # Exemplo de como você pode acessar os dados do JSON
    if json_dados and chave in json_dados:
        return json_dados[chave]
    return None

# Chamada da função para pegar o JSON
json_dados, erro = obter_json_draft5_furia()

