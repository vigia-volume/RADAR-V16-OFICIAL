import os
import time
import json
import threading
import requests
from flask import Flask
from websocket import create_connection

# --- DNA DE COMBATE ---
DERIV_TOKEN = "Vdq55rY6rqhULRF"
TELEGRAM_TOKEN = "8080389321:AAEo3_kEGP9Z0dFpIOmGHocNhp012LcV13Q"
CHAT_ID = "6672755918"

# --- ESTRATÉGIA ---
martingale = [1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0]
nivel = 0
pausa_tativa = 0

app = Flask(__name__)
@app.route('/')
def home(): return "Shine Operacional", 200

def enviar_msg(texto):
    def post():
        try: requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": texto}, timeout=5)
        except: pass
    threading.Thread(target=post).start()

def abrir_ordem(tipo, valor):
    global nivel, pausa_tativa
    print(f"🔥 EXAUSTÃO DETECTADA! Entrando com ${valor}")
    # O comando de compra real via WebSocket vai aqui
    enviar_msg(f"🎯 Shine atacou: {tipo} de ${valor}")
    pausa_tativa = 2 # Ativa a pausa de 2 velas

def radar_mercado():
    global nivel, pausa_tativa
    ws = create_connection("wss://ws.binaryws.com/websockets/v3?app_id=1089")
    ws.send(json.dumps({"authorize": DERIV_TOKEN}))
    
    while True:
        if pausa_tativa > 0:
            print(f"⏳ Aguardando pausa de {pausa_tativa} min...")
            pausa_tativa -= 1
            time.sleep(60)
            continue

        # Puxa as últimas 7 velas (6 para média + 1 atual)
        ws.send(json.dumps({"ticks_history": "R_75", "end": "latest", "count": 7, "granularity": 60, "style": "candles"}))
        dados = json.loads(ws.recv())
        
        if "candles" in dados:
            velas = dados["candles"]
            v_atual = velas[-1]["volume"]
            v_passados = [v["volume"] for v in velas[:-1]]
            media = sum(v_passados) / 6
            
            print(f"Volume Atual: {v_atual} | Média(6): {media:.2f}")

            if v_atual >= (media * 2.0):
                abrir_ordem("REVERSÃO", martingale[nivel])
                # Simulação de resultado para o Martingale
                nivel = (nivel + 1) % 7 
        
        time.sleep(60)

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))).start()
    radar_mercado()
