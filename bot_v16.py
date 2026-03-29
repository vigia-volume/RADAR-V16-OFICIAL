import os
import asyncio
from flask import Flask
from deriv_api import DerivAPI

app = Flask(__name__)

# --- PARÂMETROS DO COMANDANTE ---
TOKEN = 'oUaw8xfV2i54wpQ'
SYMBOL = 'R_75'
STAKE_INICIAL = 0.35
META_LUCRO = 10.0
MAX_MARTINGALE = 7

async def motor_v75_sniper():
    print("--- SISTEMA INICIADO: AGUARDANDO CONEXÃO DERIV ---", flush=True)
    try:
        api = DerivAPI(app_id=1089)
        await api.authorize(TOKEN)
        print("--- AUTORIDADE V75 CONFIRMADA! ---", flush=True)
        
        while True:
            print(f"--- RASTREANDO V75 | META $10 | ENTRADA BASE $0.35 ---", flush=True)
            await asyncio.sleep(20) # Intervalo de varredura

    except Exception as e:
        print(f"ERRO DE CONEXÃO: {e}", flush=True)

@app.route('/')
def home():
    return "RADAR V16 OPERACIONAL"

def start_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(motor_v75_sniper())
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    start_bot()
