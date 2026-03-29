import os
import time
import asyncio
from deriv_api import DerivAPI

TOKEN = os.environ.get('DERIV_TOKEN')
ATIVO = "R_75" 
VALORES_MARTINGALE = [1.0, 2.2, 4.8, 10.5, 23.0, 51.0, 112.0]
PAUSA_RECUPERACAO = 1800 

async def radar_v16():
    if not TOKEN:
        print("ERRO: Token não encontrado. Configure o DERIV_TOKEN no Render.")
        return
    api = DerivAPI(token=TOKEN)
    print(f"--- RADAR V16 OFICIAL ATIVADO ---")
    while True:
        try:
            candles = await api.ticks_history({'ticks_history': ATIVO, 'count': 7, 'granularity': 900})
            volumes = [c['volume'] for c in candles['candles']]
            vol_atual = volumes[-1]
            media_vol = sum(volumes[:-1]) / 6
            climax = vol_atual / media_vol if media_vol > 0 else 0
            print(f"M15 - Volume: {vol_atual:.2f} | Média: {media_vol:.2f} | Clímax: {climax:.2f}x")
            if climax >= 2.0:
                print(f"!!! CLÍMAX 2.0 DETECTADO !!!")
                await asyncio.sleep(PAUSA_RECUPERACAO)
            await asyncio.sleep(60)
        except Exception as e:
            print(f"Erro: {e}")
            await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(radar_v16())
