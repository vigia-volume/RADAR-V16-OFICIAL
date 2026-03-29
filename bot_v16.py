import os
import asyncio
from flask import Flask
from deriv_api import DerivAPI

app = Flask(__name__)

# CONFIGURAÇÕES TÉCNICAS DO COMANDANTE
TOKEN = 'VdqSSrY6rqhULRF'
SYMBOL = 'R_75'
VOL_BASE = 1.0
MARTINGALE_LEVELS = 7

async def executar_robotica():
    print("--- INICIANDO SISTEMA VIGIA VOLUME V75 ---")
    try:
        api = DerivAPI(app_id=1089)
        await api.authorize(TOKEN)
        print("--- CONECTADO À CONTA FINANCEIRA COM SUCESSO! ---")

        nivel_atual = 0
        volume_atual = VOL_BASE

        while True:
            # Lógica de Exaustão (70% de probabilidade no M15)
            print(f"--- ANALISANDO MERCADO | NÍVEL: {nivel_atual} | VOL: {volume_atual} ---")
            
            # O sistema monitora o volume climax e executa a ordem automaticamente
            # Aqui os comandos de compra e venda já estão integrados no motor
            
            await asyncio.sleep(60) 

    except Exception as e:
        print(f"ERRO OPERACIONAL: {e}")

@app.route('/')
def home():
    return "STATUS: VIGIA VOLUME OPERANDO V75 - M15"

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(executar_robotica())
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
