import asyncio
import threading
import json
import uuid

class UDPListener:

    def __init__(self, uuid=str(uuid.uuid4()), ip='0.0.0.0', port=8001):
        self._ip = ip
        self._port = port
        self._uuid = uuid
        self._callbacks = {
            'unknown': lambda json_data, addr: print(f"Unknown message received: {json_data}")
        }


    def add_callback(self, message_type, callback):
        self._callbacks[message_type] = callback

    async def listen_loop(self):
        loop = asyncio.get_running_loop()

        # Create datagram endpoint
        transport, _ = await loop.create_datagram_endpoint(
            lambda: self,
            local_addr=(self._ip, self._port)
        )

        try:
            while True:
                await asyncio.sleep(1)  # Keep the listener running
        finally:
            transport.close()

    def start(self):
        threading.Thread(target=lambda: asyncio.run(self.listen_loop())).start()



    def connection_made(self, transport):
        self.transport = transport
        print(f"Listening on {self._ip}:{self._port}")

    def datagram_received(self, data, addr):
        message = data.decode()
        try:
            json_data = json.loads(message)

            # Check json schema
            if ('uuid' in json_data) and ('message_type' in json_data) and ('content' in json_data): pass
            else: return
        
            # Filter out messages from self
            if json_data['uuid'] != self._uuid: pass
            else: return

            # Route message to callback
            message_type = json_data['message_type']
            if message_type in self._callbacks:
                self._callbacks[message_type](json_data, addr)
            else:
                self._callbacks['unknown'](json_data, addr)

        except json.JSONDecodeError:
            print(f"Received non-JSON data: {message}")

    def error_received(self, exc):
        print(f"Error received: {exc}")

    def connection_lost(self, exc):
        print("Connection lost")
