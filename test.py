import time
import asyncio
import websockets

async def hello():
    async with websockets.connect("wss://lonedark.com") as websocket:
        print("Connected")
        start=time.time()
        for i in range(1000):
            recv=await websocket.recv()
        spend=time.time()-start
        print("Received 1000 messages in %.2f seconds" % spend)
        print("Received %.2f messages per second" % (1000/spend))
        start=time.time()
        for i in range(1000):
            await websocket.send("Hello, world!")
        spend=time.time()-start
        print("Sent 1000 messages in %.2f seconds" % spend)
        print("Sent %.2f messages per second" % (1000/spend))
        print("Disconnected")

asyncio.get_event_loop().run_until_complete(hello())