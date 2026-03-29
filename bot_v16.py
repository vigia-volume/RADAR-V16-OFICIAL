import asyncio
import websockets
import json
import os

# CONFIGURAÇÕES DO COMANDANTE
TOKEN = os.getenv('TOKEN_DERIV')
APP_ID = '1089' # App ID padrão

async def radar_v16():
    url = f"wss://ws.binaryws.com/websockets/v3?app_id={APP_ID}"
    
    async with websockets.connect(url) as websocket:
        print("--- RADAR V16: CONEXÃO ESTABELECIDA COM SUCESSO ---")
        
        # Autenticação
        await websocket.send(json.dumps({"authorize": TOKEN}))
        response = await websocket.recv()
        print(f"Status de Autenticação: {json.loads(response).get('msg_type')}")

        # Inscrição no Bitcoin (BTC/USD)
        subscribe_msg = json.dumps({"ticks": "cryBTCUSD"})
        await websocket.send(subscribe_msg)

        async for message in websocket:
            data = json.loads(message)
            if 'tick' in data:
                preco = data['tick']['quote']
                print(f"Monitorando BTC: {preco} | Radar em QAP...")

if __name__ == "__main__":
    asyncio.run(radar_v16())
