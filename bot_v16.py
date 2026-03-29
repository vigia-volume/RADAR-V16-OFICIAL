import os, threading, asyncio, time
from flask import Flask
from deriv_api import DerivAPI

TOKEN = 'VdqSSrYBtghuLRFi'
APP_ID = '1089' 

app = Flask(__name__)
@app.route('/')
def home(): return "ROBÔ V75 - MARTINGALE 7 NÍVEIS ATIVO", 200

async def loop_martingale():
    api = DerivAPI(app_id=APP_ID)
    await api.authorize(TOKEN)
    
    # Tabela de Martingale (Volume 1.0 inicial)
    niveis = [1.0, 2.1, 4.5, 9.5, 20.0, 42.0, 88.0]
    indice = 0

    while True:
        valor_atual = niveis[indice]
        print(f"[{time.strftime('%H:%M:%S')}] Ordem Nível {indice+1}: Vol {valor_atual}")
        
        try:
            # Executa Rise (CALL) de 1 minuto
            compra = await api.buy({"buy": 1, "price": 100, "parameters": {"amount": valor_atual, "basis": "stake", "contract_type": "CALL", "currency": "USD", "duration": 1, "duration_unit": "m", "symbol": "R_75"}})
            contract_id = compra['buy']['contract_id']
            
            # Aguarda 65s para resultado
            await asyncio.sleep(65)
            
            # Verifica Resultado
            check = await api.forget_all('proposal_open_contract')
            status = await api.proposal_open_contract({"proposal_open_contract": 1, "contract_id": contract_id})
            resultado = status['proposal_open_contract']['status'] # 'won' ou 'lost'

            if resultado == 'won':
                print("VITÓRIA! Resetando Martingale.")
                indice = 0
            else:
                print("DERROTA. Subindo nível.")
                indice = (indice + 1) if indice < 6 else 0 # Reseta se passar do 7º nível

        except Exception as e:
            print(f"Erro: {e}")
            await asyncio.sleep(10)

if __name__ == "__main__":
    threading.Thread(target=lambda: asyncio.run(loop_martingale()), daemon=True).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

