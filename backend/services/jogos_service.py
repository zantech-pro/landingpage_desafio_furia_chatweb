from services.json_service import obter_json_draft5_furia
from datetime import datetime

def buscar_proximos_jogos_furia():
    json_data, erro = obter_json_draft5_furia()

    if erro or not json_data:
        return "❌ Erro ao acessar dados dos jogos no draft5.gg."

    try:
        partidas = json_data["props"]["pageProps"]["matches"]
        jogos_futuros = [j for j in partidas if not j.get("isFinished") and not j.get("isOver")]

        if not jogos_futuros:
            return "📭 A FURIA não tem jogos marcados no momento."

        resposta = ["🎯 Próximos jogos da FURIA:"]
        for jogo in jogos_futuros[:5]:
            adversario = jogo.get("opponentTeamName", "Adversário desconhecido")
            evento = jogo.get("tournament", {}).get("tournamentName", "Evento não informado")
            timestamp = jogo.get("matchDate")
            
            if isinstance(timestamp, int):
                data = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y")
            else:
                data = "Data não disponível"

            resposta.append(f"- {data}: vs {adversario} ({evento})")

        resposta.append("\nVeja mais em: https://draft5.gg/equipe/330-FURIA")
        return "\n".join(resposta)

    except KeyError as ke:
        return f"❌ Erro ao acessar a chave no JSON: {str(ke)}"
    except Exception as e:
        return f"❌ Erro ao processar os dados dos jogos: {str(e)}"
