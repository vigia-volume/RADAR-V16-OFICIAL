import asyncio
import websockets
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# --- PORTA FALSA PARA O RENDER NÃO TRAVAR ---
def run_fake_server():
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"RADAR V16 ONLINE")
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), Handler)
    server.serve_forever()

# --- RADAR DO COMANDANTE ---
TOKEN = os.getenv('TOKEN_DERIV')

async def radar_v16():
    url = "wss://ws.binaryws.com/websockets/v3?app_id=1089"
    async with websockets.connect(url) as websocket:
        print("--- RADAR V16: CONEXÃO ESTABELECIDA ---")
        await websocket.send(json.dumps({"authorize": TOKEN}))
        await websocket.send(json.dumps({"ticks": "cryBTCUSD"}))
        async for message in websocket:
            data = json.loads(message)
            if 'tick' in data:
                print(f"BTC: {data['tick']['quote']} | Monitorando...")

if __name__ == "__main__":
    # Liga o servidor falso em uma linha separada
    threading.Thread(target=run_fake_server, daemon=True).start()
    # Liga o Radar
    asyncio.run(radar_v16())

