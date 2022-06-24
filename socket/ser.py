import socket

HOST = '192.168.1.179'
PORT = 8000
# 1.
clientSocket = socket.socket()

# 2. 连接远程主机
clientSocket.connect((HOST, PORT))

# 3. 客户端， 服务端通信
# 给server主机发送消息
clientSocket.send(b'hello server')
# 接收服务端的响应(即服务端回复的消息)
recvData = clientSocket.recv(1024).decode('utf-8')
print("接收到服务器的消息:", recvData)
# 4. 关闭socket对象:
clientSocket.close()
