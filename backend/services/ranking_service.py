from services.json_ranking_service import obter_json_dos_links
def buscar_ranking_furia():
    # URLs para rankings
    url_americas = "https://draft5.gg/ranking"  # Link para o ranking das Américas
    url_global = "https://draft5.gg/ranking?region=global"  # Link para o ranking Global

    # Obter ranking das Américas
    json_americas, erro_americas = obter_json_dos_links(url_americas)
    if erro_americas:
        return f"Erro ao obter ranking das Américas: {erro_americas}"

    # Obter ranking Global
    json_global, erro_global = obter_json_dos_links(url_global)
    if erro_global:
        return f"Erro ao obter ranking Global: {erro_global}"

    try:
        # Buscar os rankings da FURIA nas duas regiões (global e américas)
        def buscar_ranking(json_data, regiao=None):
            ranking_data = json_data.get("props", {}).get("pageProps", {}).get("valveDetails", {}).get("data", [])
            if not ranking_data:
                return None

            # Filtrar o ranking da FURIA
            furia_entrada = next((t for t in ranking_data if t.get("rankingValveTeamName") == "FURIA" and (not regiao or t.get("rankingValveRegion") == regiao)), None)
            if not furia_entrada:
                return None

            posicao = ranking_data.index(furia_entrada) + 1  # +1 pois o índice começa de 0
            pontos_furia = furia_entrada.get("rankingValvePoints")
            lineup_furia = furia_entrada.get("rankingValveLineup")
            return posicao, pontos_furia, lineup_furia

        # Buscar FURIA no ranking global
        posicao_global, pontos_furia_global, lineup_furia_global = buscar_ranking(json_global)

        # Buscar FURIA no ranking das Américas
        posicao_americas, pontos_furia_americas, lineup_furia_americas = buscar_ranking(json_americas, regiao="americas")

        # Preparar a resposta
        resposta = "🏆 Ranking da Valve da FURIA:\n\n"

        # Ranking Global
        if posicao_global:
            resposta += f"🌍 Ranking Global:\n"
            resposta += f"🔝 Posição: {posicao_global}\n"
            resposta += f"🔢 Pontuação: {pontos_furia_global} pts\n"
            resposta += f"👥 Line-up: {lineup_furia_global}\n\n"
        else:
            resposta += "🌍 A FURIA não está no ranking global.\n\n"

        # Ranking Américas
        if posicao_americas:
            resposta += f"🌎 Ranking Américas:\n"
            resposta += f"🔝 Posição: {posicao_americas}\n"
            resposta += f"🔢 Pontuação: {pontos_furia_americas} pts\n"
            resposta += f"👥 Line-up: {lineup_furia_americas}\n"
        else:
            resposta += "🌎 A FURIA não está no ranking das Américas.\n"

        return resposta

    except Exception as e:
        return f"❌ Erro ao processar os dados do ranking: {e}"