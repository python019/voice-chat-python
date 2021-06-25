from vidstream import AudioSender
from vidstream import AudioReceiver 

import threading
import socket

receiver = AudioReceiver('192.168.43.121', 9999)
receive_thread = threading.Thread(target=receiver.start_server)

sender = AudioSender("192.168.43.121", 5555)
sender_thread = threading.Thread(target=sender.start_stream)

receive_thread.start()
sender_thread.start()

