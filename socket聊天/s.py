import socket
from concurrent.futures import ThreadPoolExecutor

server = socket.socket()
server.bind(('127.0.0.1',9500))
server.listen(5)

#封装成一个函数
def run(conn):
    while True:
        try:
            data = conn.recv(1024)
            if len(data) == 0:
                break
            print(data.decode('utf-8'))
            conn.send('好啊'.encode('utf-8'))
        except Exception as e:
            print(e)
            break
    conn.close()
if __name__ == '__main__':
    print('Server is running')
    pool = ThreadPoolExecutor(10)
    while True:
        conn,addr = server.accept()
        pool.submit(run,conn)
