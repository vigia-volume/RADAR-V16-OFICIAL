import websocket
import json
import threading
from flask import Flask
import os

app = Flask(__name__)

# CONFIGURAÇÕES DE COMBATE - DERIV
TOKEN = "COLE_SEU_TOKEN_AQUI" 
APP_ID = "1089" 
SYMBOL = "R_75" 

@app.route('/')
def home():
    return "OPERANTE - AGUARDANDO COMANDO"

def abrir_ordem(ws):
    print("--- ATACANDO AGORA NO VOLATILITY 75 ---")
    # Comando direto de compra (CALL) de 1 minuto
    payload = {
        "buy": 1,
        "price": 1,
        "parameters": {
            "amount": 1.0,
            "basis": "stake",
            "contract_type": "CALL",
            "currency": "USD",
            "duration": 1,
            "duration_unit": "m",
            "symbol": SYMBOL
        }
    }
    ws.send(json.dumps(payload))

def on_message(ws, message):
    dados = json.loads(message)
    
    # 1. Autenticação bem-sucedida
    if "authorize" in dados:
        print("Autenticado na Deriv! Disparando ordem de teste...")
        abrir_ordem(ws)
    
    # 2. Resposta da Ordem
    if "buy" in dados:
        if "error" in dados:
            print(f"ERRO DERIV: {dados['error']['message']}")
        else:
            print("FOI! Ordem aberta com sucesso na conta.")

def on_open(ws):
    auth_data = {"authorize": TOKEN}
    ws.send(json.dumps(auth_data))

def iniciar_bot():
    url = f"wss://ws.binaryws.com/websockets/v3?app_id={APP_ID}"
    ws = websocket.WebSocketApp(url, on_open=on_open, on_message=on_message)
    ws.run_forever()

if __name__ == "__main__":
    threading.Thread(target=iniciar_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

