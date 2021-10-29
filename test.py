import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://lorddimension.com/ws") as websocket:
        print("Connected")
        async for message in websocket:
            await websocket.send(message)
        print("Disconnected")

asyncio.get_event_loop().run_until_complete(hello())