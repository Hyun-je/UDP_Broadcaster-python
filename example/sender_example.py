import asyncio
import time
from udp_broadcaster import UDPSender

sender = UDPSender()

while True:
    time.sleep(1)
    message_type = 'device_ping'
    content = {}
    sender.send_dict(message_type, content)
    print('send ping...')