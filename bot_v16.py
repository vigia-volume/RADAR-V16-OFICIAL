import os
import time
import requests
import threading
from flask import Flask

# --- DNA DA SHINE (DADOS OFICIAIS DA FOTO) ---
TELEGRAM_TOKEN = "8080389321:AAEo3_kEGP9Z0dFpIOmGHocNhp012LCv13Q"
CHAT_ID = "6672755918"
DERIV_TOKEN = "Vdq55rY6rqhULRF"

# --- SISTEMA DE MANUTENÇÃO (RENDER) ---
app = Flask(__name__)
@app.route('/')
def home():
    return "Shine v16.1 Online", 200

def run_flask():
    # O Render usa a porta 10000 por padrão
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# --- SISTEMA DE RÁDIO ---
def enviar_alerta(mensagem):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensagem}
    try:
        response = requests.post(url, json=payload)
        print(f"Status do Telegram: {response.status_code}")
    except Exception as e:
        print(f"Erro ao enviar: {e}")

# --- MOTOR DE VIGIA M1 ---
def radar_shine():
    print("Iniciando radar de exaustão...")
    # Pequeno delay para o Flask subir primeiro
    time.sleep(5)
    enviar_alerta("🚀 Comandante, Shine v16.1 Online! O rádio foi calibrado e o radar M1 está operando.")
    
    while True:
        msg_vigia = "🛰️ Shine M1: Radar ativo. Tudo normal na frequência."
        print(msg_vigia)
        enviar_alerta(msg_vigia)
        time.sleep(60) # Ciclo de 1 minuto

if __name__ == "__main__":
    # Inicia o servidor para o Render não dar erro
    threading.Thread(target=run_flask).start()
    # Inicia o radar
    radar_shine()
