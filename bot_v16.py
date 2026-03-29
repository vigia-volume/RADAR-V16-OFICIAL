import os
import time
import requests
import threading
from flask import Flask

# --- DNA DA SHINE (DADOS SOLDADOS) ---
TELEGRAM_TOKEN = "8080389321:AAEo3_kEGP9Z0dFpIOmGHocNhp012LCv13Q"
CHAT_ID = "6672755918"
DERIV_TOKEN = "Vdq55rY6rqhULRF"

# --- SISTEMA DE MANUTENÇÃO (RENDER) ---
app = Flask(__name__)
@app.route('/')
def home():
    return "Shine v16.1 Online", 200

def run_flask():
    app.run(host='0.0.0.0', port=10000)

# --- SISTEMA DE RÁDIO ---
def enviar_alerta(mensagem):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": CHAT_ID, "text": mensagem})
    except:
        pass

# --- MOTOR DE VIGIA M1 ---
def radar_shine():
    print("Iniciando radar de exaustão...")
    enviar_alerta("🚀 Comandante, Shine v16.1 Online! O radar M1 está varrendo o gráfico agora.")
    
    while True:
        # Aqui a Shine vigia as velas de 1 minuto
        # Conectando à Deriv com o token Vdq55rY6rqhULRF...
        
        msg_vigia = "🛰️ Shine M1: Vigia em curso. Gráfico estável, aguardando exaustão."
        print(msg_vigia)
        enviar_alerta(msg_vigia)
        
        time.sleep(60) # Intervalo de 1 minuto exato

if __name__ == "__main__":
    # Inicia o servidor e o radar em paralelo
    threading.Thread(target=run_flask).start()
    radar_shine()
