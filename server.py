#!/usr/bin/env python
import pyaudio
import socket
import sys
import socketserver

# Pyaudio Initialization
chunk = 1024
pa = pyaudio.PyAudio()

# Opening of the audio stream
stream = pa.open(format = 8,
                channels = 1,
                rate = 10240,
                output = True)

# Socket Initialization
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)     # For using same port again
s.bind((socket.gethostname(), 1234))
size = 1024
s.listen(5)
client, address = s.accept()


print('Server Running...')
while 1:
    data = client.recv(size)
    if data:
        stream.write(data)  # Stream the recieved audio data
        client.send(b'ACK')  # Send back Acknowledgement, has to be in binary form

client.close()
stream.close()
pa.terminate()
print("Server has stopped running")
