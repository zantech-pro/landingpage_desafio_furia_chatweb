import os
from google.cloud import dialogflow_v2 as dialogflow

# Configurações do Dialogflow
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./chatiafera-8399272823a5.json"
project_id = "chatiafera"
language_code = "pt-BR"

def detect_intent_texts(session_id, text):
    client = dialogflow.SessionsClient()
    session = client.session_path(project_id, session_id)

    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)

    response = client.detect_intent(session=session, query_input=query_input)

    fulfillment_text = response.query_result.fulfillment_text
    intent_name = response.query_result.intent.display_name

    return fulfillment_text, intent_name
