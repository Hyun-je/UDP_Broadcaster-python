import asyncio
import time
from udp_broadcaster import UDPPeriodicSender


def data_callback():
    message_type = 'device_ping'
    content = {}
    return message_type, content


sender = UDPPeriodicSender(interval=1, data_callback=data_callback)

sender.start()

while True:
    pass

