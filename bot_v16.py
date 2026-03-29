import websocket
import json
import threading
from flask import Flask
import os

app = Flask(__name__)

# CONFIGURAÇÕES DE COMBATE - DADOS RESGATADOS
TOKEN = "V68YfE6G7i5X6Tj" # Token de Negociação (Trade)
APP_ID = "61546" # Seu App ID da Deriv
SYMBOL = "R_75" 

@app.route('/')
def home():
    return "OPERANTE - ATAQUE DIRETO EM CURSO"

def abrir_ordem(ws):
    print("--- DISPARANDO AGORA NO VOLATILITY 75 ---")
    # Comando de compra (CALL) imediato
    payload = {
        "buy": 1,
        "price": 100, # Preço máximo aceitável
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
    
    # 1. Autenticação
    if "authorize" in dados:
        if "error" in dados:
            print(f"ERRO DE AUTENTICAÇÃO: {dados['error']['message']}")
        else:
            print("AUTENTICADO! DISPARANDO TIRO DE TESTE...")
            abrir_ordem(ws)
    
    # 2. Resposta da Compra
    if "buy" in dados:
        if "error" in dados:
            print(f"ERRO NA OPERAÇÃO: {dados['error']['message']}")
        else:
            print("ORDEM EXECUTADA COM SUCESSO NA DERIV!")

def on_open(ws):
    auth_data = {"authorize": TOKEN}
    ws.send(json.dumps(auth_data))

def iniciar_bot():
    url = f"wss://ws.binaryws.com/websockets/v3?app_id={APP_ID}"
    ws = websocket.WebSocketApp(url, on_open=on_open, on_message=on_message)
    ws.run_forever()

if __name__ == "__main__":
    # Inicia o motor em segundo plano
    threading.Thread(target=iniciar_bot, daemon=True).start()
    
    # Porta padrão para o Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
