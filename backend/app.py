from flask import Flask, render_template
from flask_cors import CORS
from routes.webhook import webhook_bp



app = Flask(__name__)

# Adicionando CORS para permitir todas as origens
CORS(app, resources={r"/*": {"origins": "*"}})

# Registrar rotas separadas
app.register_blueprint(webhook_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False, port=5000)
