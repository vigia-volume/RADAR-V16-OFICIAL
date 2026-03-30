import os
import asyncio
import threading
from flask import Flask
from deriv_api import DerivAPI

app = Flask(__name__)

# --- PARÂMETROS DO COMANDANTE ---
TOKEN_V16 = 'IPDjayR4OrX6yHU'
SYMBOL = 'R_75'
STAKE_INICIAL = 0.35

@app.route('/')
def home():
    return "RADAR V16: AMBIENTE DEMO ATIVO"

async def motor_ofensivo():
    token_limpo = TOKEN_V16.strip().replace(" ", "")
    print(f"--- 🚀 INICIANDO CONEXÃO: {token_limpo[:4]}... ---", flush=True)
    
    try:
        api = DerivAPI(app_id=1089)
        await api.authorize(token_limpo)
        print("--- ✅ AUTORIDADE CONFIRMADA! CONECTADO! ---", flush=True)
        
        while True:
            print(f"--- 📡 MONITORANDO V75 | STAKE $0.35 ---", flush=True)
            await asyncio.sleep(20)

    except Exception as e:
        print(f"--- ❌ ERRO DE RESPOSTA: {e} ---", flush=True)

def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(motor_ofensivo())

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
