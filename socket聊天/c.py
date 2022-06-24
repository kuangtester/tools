import socket


client = socket.socket()
client.connect(('127.0.0.1',9500))
print('Client is running')
while True:
    msg = input('客户端：').encode('utf-8')
    client.send(msg)
    data = client.recv(1024)
    print(data.decode('utf-8'))
