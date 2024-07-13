import asyncio
import threading
from udp_broadcaster import UDPListener

def callback_ping_message(json_data, addr):
    print(f"Ping message received: {json_data}")


listener = UDPListener(
    uuid="S3K0LS23WB",
    ip='0.0.0.0',
    port=8001
)

listener.add_callback('device_ping', callback_ping_message)

listener.start()

while True:
    pass