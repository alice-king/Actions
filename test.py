import time
import asyncio
import websockets

async def hello(host):
    async with websockets.connect(host,max_size=2**32,ping_interval=60) as websocket:
        print("Connected:"+str(websocket.local_address))

        recv=await websocket.recv()
        start=time.time()
        for i in range(1000):
            recv=await websocket.recv()
        spend=time.time()-start
        await websocket.send(str(spend))
        print("Received 1000 messages in %.2f seconds" % spend)
        print("Received %.2f messages per second" % (1000/spend))

        await websocket.send("Hello, world!")
        for i in range(1000):
            await websocket.send("Hello, world!")
        spend=float(await websocket.recv())
        print("Sent 1000 messages in %.2f seconds" % spend)
        print("Sent %.2f messages per second" % (1000/spend))

        recv=await websocket.recv()
        start=time.time()
        recv=await websocket.recv()
        spend=time.time()-start
        await websocket.send(str(spend))
        print("Received 1MB in %.2f seconds" % spend,len(recv))
        print("Received %.2fMB per second" % (1/spend))

        await websocket.send("Hello, world!")
        await websocket.send(bytes(1048576))
        spend=float(await websocket.recv())
        print("Sent 1MB in %.2f seconds" % spend)
        print("Sent %.2fMB per second" % (1/spend))

        print("Disconnected")

# asyncio.get_event_loop().run_until_complete(hello("ws://localhost/websocket/"))
# asyncio.get_event_loop().run_until_complete(hello("wss://api.lonedark.ml/websocket/"))
asyncio.get_event_loop().run_until_complete(hello("ws://api.lonedark.ml/websocket/"))
asyncio.get_event_loop().run_until_complete(hello("ws://[2a02:180:6:1::4c35]:9001/websocket/"))
