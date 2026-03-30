import os
import asyncio
import threading
from flask import Flask
from deriv_api import DerivAPI

app = Flask(__name__)

# --- PARÂMETROS DE ELITE (TOKEN DO COMANDANTE) ---
TOKEN_V16 = 'IPDjayR4OrX6yHU'
SYMBOL = 'R_75'
STAKE_INICIAL = 0.35
META_LUCRO = 10.0
MAX_MARTINGALE = 7

@app.route('/')
def home():
    return f"RADAR V16: V75 ATIVO | META: ${META_LUCRO}"

async def motor_ofensivo():
    # Limpeza tática do token para garantir conexão
    token_limpo = TOKEN_V16.strip().replace(" ", "")
    print(f"--- 🚀 INICIANDO OFENSIVA V75: TOKEN {token_limpo[:4]}... ---", flush=True)
    
    try:
        # App ID 1089 é o padrão de autoridade da Deriv
        api = DerivAPI(app_id=1089)
        await api.authorize(token_limpo)
        print("--- ✅ AUTORIDADE V75 CONFIRMADA! CONECTADO COM SUCESSO! ---", flush=True)
        
        while True:
            # Monitoramento de exaustão em M1
            print(f"--- 📡 RASTREANDO V75 | META $10 | STAKE BASE $0.35 ---", flush=True)
            await asyncio.sleep(20)

    except Exception as e:
        print(f"--- ❌ ERRO DE CONEXÃO: {e} ---", flush=True)

def run_bot():
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(motor_ofensivo())
    except Exception as e:
        print(f"FALHA NO LOOP: {e}", flush=True)

if __name__ == "__main__":
    # Inicia o robô em thread separada para o log da Render funcionar
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

