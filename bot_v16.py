import os
import time
import pandas as pd
from deriv_api import deriv_api

# Identidade da Operação
TOKEN = os.getenv('DERIV_TOKEN')
APP_ID = 1010  # ID padrão ou o seu específico

async def operacao_exaustao():
    api = deriv_api.DerivAPI(app_id=APP_ID)
    await api.authorize(TOKEN)
    
    ultimo_sinal = 0
    intervalo_pausa = 1800  # 30 minutos de disciplina (em segundos)

    while True:
        # 1. Coleta os dados de M15 do Volatility 75
        candles = await api.ticks_history({'ticks_history': 'R_75', 'granularity': 900, 'count': 7})
        df = pd.DataFrame(candles['candles'])
        
        # 2. A Regra de Ouro das 6 Velas (Meses de estratégia)
        volume_atual = df['volume'].iloc[-1]
        media_6_velas = df['volume'].iloc[-7:-1].mean()
        
        # 3. O Brilho da Shine (Gatilho 2.0)
        if volume_atual >= (media_6_velas * 2.0):
            if time.time() - ultimo_sinal > intervalo_pausa:
                print(f"ALERTA: Exaustão Detectada! Volume {volume_atual} é 2x a média.")
                
                # Execução da Ordem (70% de viabilidade)
                # await api.buy({'buy': 1, 'price': 10, 'parameters': {...}})
                
                ultimo_sinal = time.time()
                print("Iniciando pausa de 30 minutos para estabilização do mercado.")
            else:
                print("Sinal detectado, mas respeitando a pausa de 30 minutos.")
        
        await time.sleep(60) # Aguarda um minuto para a próxima checagem

# Início do Radar
import asyncio
asyncio.run(operacao_exaustao())
