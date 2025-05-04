import nest_asyncio
nest_asyncio.apply()
from flask import Blueprint, request, jsonify
from services.dialogflow_service import detect_intent_texts
from services.jogos_service import buscar_proximos_jogos_furia
from services.noticias_service import buscar_noticias_furia
from services.elenco_service import buscar_elenco_furia  
from services.ranking_service import buscar_ranking_furia  
from services.loja_service import buscar_loja_furia  
import os

webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    user_message = req.get('message', '')

    if not user_message:
        return jsonify({'error': 'Nenhuma mensagem recebida'}), 400

    session_id = "sessao-" + os.urandom(8).hex()
    fulfillment_text, intent_name = detect_intent_texts(session_id, user_message)

    if intent_name == "ProximosJogosFuria":
        fulfillment_text = buscar_proximos_jogos_furia()
    elif intent_name == "NoticiasFURIA":
        fulfillment_text = buscar_noticias_furia()
    elif intent_name == "ElencoFURIA":
        fulfillment_text = buscar_elenco_furia()
    elif intent_name == "RankingFURIA":
        fulfillment_text = buscar_ranking_furia()
    elif intent_name == "LojaFURIA":
        fulfillment_text = buscar_loja_furia()

    return jsonify({
        'reply': fulfillment_text
    })
