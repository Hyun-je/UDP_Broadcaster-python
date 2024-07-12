import asyncio
from udp_broadcaster import UDPListener

def on_received_message(data, addr):
    print(data, addr)

listener = UDPListener(
    uuid="S3K0LS23WB",
    ip='0.0.0.0',
    port=8001,
    callback=on_received_message
)

asyncio.run(listener.listen())