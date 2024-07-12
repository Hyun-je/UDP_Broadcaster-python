import asyncio
import socket
import time
import uuid
import threading

from . import UDPSender


class UDPPeriodicSender(UDPSender):

    def __init__(self, interval, data_callback, uuid=str(uuid.uuid4())):
        super().__init__(uuid)
        self._interval = interval
        self._data_callback = data_callback

    async def send_loop(self):
        while True:
            await asyncio.sleep(self._interval)
            message_type, content = self._data_callback()
            self.send_dict(message_type, content)

    def start(self):
        threading.Thread(target=lambda: asyncio.run(self.send_loop())).start()