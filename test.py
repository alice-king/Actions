import time
import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://lorddimension.com/ws") as websocket:
        print("Connected")
        start=time.time()
        for i in range(100):
            recv=await websocket.recv()
        spend=time.time()-start
        print("Received 100 messages in %.2f seconds" % spend)
        print("Received %.2f messages per second" % (100/spend))
        start=time.time()
        for i in range(100):
            await websocket.send("Hello, world!")
        spend=time.time()-start
        print("Sent 100 messages in %.2f seconds" % spend)
        print("Sent %.2f messages per second" % (100/spend))
        print("Disconnected")

asyncio.get_event_loop().run_until_complete(hello())