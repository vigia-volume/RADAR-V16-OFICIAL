import os
import time
import requests
import threading
from flask import Flask

# --- DNA DA SHINE (REVISADO E LIMPO) ---
# Copie exatamente como está abaixo, sem espaços extras
TELEGRAM_TOKEN = "8080389321:AAEo3_kEGP9Z0dFpIOmGHocNhp012LcV13Q"
CHAT_ID = "6672755918"
DERIV_TOKEN = "Vdq55rY6rqhULRF"

app = Flask(__name__)
@app.route('/')
def home():
    return "Shine v16.1 Online", 200

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def enviar_alerta(mensagem):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    try:
        r = requests.post(url, json={"chat_id": CHAT_ID, "text": mensagem})
        print(f"Tentativa de envio: {r.status_code}") # 200 é sucesso!
    except:
        pass

def radar_shine():
    print("Radar Shine iniciando...")
    time.sleep(10) # Tempo para o Render estabilizar
    enviar_alerta("🚀 Shine v16.1: Rádio sintonizado! Estou na escuta, Comandante.")
    
    while True:
        enviar_alerta("🛰️ Shine M1: Radar ativo.")
        time.sleep(60)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    radar_shine()
