import socket

from Forloop import name

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print('Socket created')
s.bind(('localhost', 9999))
s.listen(3)
print('Server listening')
while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print('Connection from', addr, name)
    c.send(bytes('Hello World!', 'utf-8'))
    c.close()

