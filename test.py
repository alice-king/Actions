import time
import asyncio
import websockets

async def hello(host):
    async with websockets.connect(host,max_size=2**32) as websocket:
    # async with websockets.connect("wss://api.lonedark.com",max_size=2**32) as websocket:
        print("Connected:"+str(websocket.local_address))
        recv=await websocket.recv()
        start=time.time()
        for i in range(1000):
            recv=await websocket.recv()
        spend=time.time()-start
        print("Received 1000 messages in %.2f seconds" % spend)
        print("Received %.2f messages per second" % (1000/spend))
        await websocket.send("Hello, world!")
        start=time.time()
        for i in range(1000):
            await websocket.send("Hello, world!")
        spend=time.time()-start
        print("Sent 1000 messages in %.2f seconds" % spend)
        print("Sent %.2f messages per second" % (1000/spend))
        recv=await websocket.recv()
        start=time.time()
        recv=await websocket.recv()
        spend=time.time()-start
        print("Received 10MB in %.2f seconds" % spend)
        print("Received %.2fMB per second" % (10/spend))
        await websocket.send("Hello, world!")
        start=time.time()
        await websocket.send(b'\x00'*10485760)
        spend=time.time()-start
        print("Sent 10MB in %.2f seconds" % spend)
        print("Sent %.2fMB per second" % (10/spend))
        print("Disconnected")

asyncio.get_event_loop().run_until_complete(hello("ws://localhost"))
asyncio.get_event_loop().run_until_complete(hello("wss://api.lonedark.com"))
