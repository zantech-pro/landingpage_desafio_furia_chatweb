from services.json_service import obter_json_draft5_furia

def buscar_elenco_furia():
    json_data, erro = obter_json_draft5_furia()
    
    if erro:
        return erro

    try:
        elenco = json_data['props']['pageProps']['data']['playerData']
        resposta = "🎯 Elenco atual da FURIA:\n\n"

        for jogador in elenco:
            nome = f"{jogador['playerFirstName']} {jogador['playerLastName']}".strip()
            nickname = jogador.get("playerNickname", "Sem nickname")
            pais = jogador.get("playerCountry", "Desconhecido")
            status = jogador.get("playerHistory", [{}])[0].get("status", "Sem status")

            resposta += f"🧑 {nickname} ({nome}) - {status}, 🇨🇵 {pais}\n"

        return resposta
    except Exception as e:
        return f"❌ Erro ao processar os dados do elenco: {e}"
