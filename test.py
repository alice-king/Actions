import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://lorddimension.com/ws") as websocket:
        for i in range(2000):
            await websocket.send("Hello world!")
            recv=await websocket.recv()
            print(recv,i)

asyncio.get_event_loop().run_until_complete(hello())