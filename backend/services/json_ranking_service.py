import requests
from bs4 import BeautifulSoup
import json

def obter_json_dos_links(url):
    try:
        # Faz a requisição HTTP para pegar o HTML da página
        resposta = requests.get(url)
        resposta.raise_for_status()  # Levanta exceção em caso de erro na requisição

        # Usa BeautifulSoup para fazer o parsing do HTML
        soup = BeautifulSoup(resposta.content, "html.parser")

        # Procura pela tag <script> que contém o JSON (vamos procurar por uma tag script específica)
        # Caso o JSON esteja dentro de uma tag <script> sem atributos específicos, pode-se pegar o primeiro script
        script_tag = soup.find("script", {"id": "__NEXT_DATA__"})  # Exemplo, ID do script com JSON

        if script_tag:
            # Extrai o conteúdo da tag <script> (que é um JSON)
            json_text = script_tag.string.strip()

            # Tenta carregar o conteúdo JSON
            json_data = json.loads(json_text)

            return json_data, None
        else:
            return None, "Não foi possível encontrar o JSON dentro da tag <script>."

    except requests.exceptions.RequestException as erro:
        return None, f"Erro ao buscar a página: {erro}"

    except json.JSONDecodeError as e:
        return None, f"Erro ao decodificar o JSON: {e}"


