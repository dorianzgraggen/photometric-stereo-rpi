import asyncio
from websockets import connect

async def hello(uri):
    async with connect(uri) as websocket:
      await websocket.send("here i am")

      while True:
        try:
            msg = await websocket.recv()
        except websockets.ConnectionClosed:
            print(f"Terminated")
            break

        print(msg)

asyncio.run(hello("ws://localhost:8080"))