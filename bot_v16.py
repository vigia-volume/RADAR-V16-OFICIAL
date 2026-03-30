import os
import asyncio
import threading
from flask import Flask
from deriv_api import DerivAPI

app = Flask(__name__)

# --- PARÂMETROS DO COMANDANTE ---
TOKEN = 'oUaw8xfV2i54wpQ'
SYMBOL = 'R_75'
STAKE_INICIAL = 0.35
META_LUCRO = 10.0

@app.route('/')
def home():
    return "RADAR V16 OPERACIONAL"

async def motor_v75_sniper():
    print("--- 🚀 INICIANDO CONEXÃO DERIV AGORA... ---", flush=True)
    try:
        api = DerivAPI(app_id=1089)
        await api.authorize(TOKEN)
        print("--- ✅ AUTORIDADE V75 CONFIRMADA! ---", flush=True)
        
        while True:
            print(f"--- 📡 RASTREANDO V75 | META $10 | STAKE $0.35 ---", flush=True)
            await asyncio.sleep(15)

    except Exception as e:
        print(f"--- ❌ ERRO DE CONEXÃO: {e} ---", flush=True)

def run_bot():
    asyncio.run(motor_v75_sniper())

if __name__ == "__main__":
    # Inicia o bot em uma linha separada para não travar o log
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
