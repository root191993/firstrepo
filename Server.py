import socket
from encodings.punycode import selective_find

s = socket.socket()
print("Socket created")
s.bind(('localhost', 9999))
s.listen(3)
print("Socket listening")

while True:
     c, addr = s.accept()
     print("Connected with", addr)

     c.send(bytes('Hello World','utf-8'))

     c.close()
