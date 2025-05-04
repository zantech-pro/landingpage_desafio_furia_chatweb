from services.json_service import obter_json_draft5_furia

def buscar_noticias_furia():
    json_data, erro = obter_json_draft5_furia()

    if erro or not json_data:
        return "❌ Erro ao acessar notícias no draft5.gg."

    try:
        # Verificando a estrutura correta e acessando as notícias
        noticias = json_data.get("props", {}).get("pageProps", {}).get("news", {}).get("data", [])

        if not noticias:
            return "📭 Nenhuma notícia recente da FURIA encontrada."

        resposta = ["📰 Últimas notícias da FURIA:"]
        for noticia in noticias[:5]:  # Mostrando as 5 últimas notícias
            titulo = noticia.get("postTitle", "Título não disponível")
            slug = noticia.get("postSlug", "")
            link = f"https://draft5.gg/noticia/{slug}" if slug else "🔗 Link indisponível"
            data = noticia.get("postDate", "Data não disponível")
            autor = noticia.get("author", {}).get("name", "Autor desconhecido")

            # Adicionando a notícia com as informações extras (data e autor)
            resposta.append(f"- [{titulo}]({link})")
            resposta.append(f"  📅 Data: {data}")
            resposta.append(f"  ✍️ Autor: {autor}")

        # Adicionando link para mais notícias
        resposta.append("\n🔗 Para mais notícias, acesse: https://draft5.gg/equipe/330")

        return "\n".join(resposta)

    except Exception as e:
        return f"❌ Erro ao processar as notícias da FURIA: {e}"
