import asyncio
import socket
import json
import time
import uuid


class UDPSender:

    def __init__(self, uuid=str(uuid.uuid4())):
        self._uuid = uuid
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def send_dict(self, message_type, content={}, ip='255.255.255.255', port=8001, verbose=False):
        dict = {
            'uuid': self._uuid, 
            'time': time.strftime('%Y-%m-%d %H:%M:%S'),
            'hostname': socket.gethostname(),
            'message_type': message_type,
            'content': content
        }
        bytes = json.dumps(dict).encode('utf-8')
        self._sock.sendto(bytes, (ip, port))
        if verbose:
            print(f"[{dict['time']}] {dict['uuid'][:8]} -> {message_type} {content}")