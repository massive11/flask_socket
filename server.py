from socket import *
import json
import os

host = '192.168.0.101'
port = 1333
ADDR = (host, port)
BUFSIZ = 1024

tcpSocket = socket(AF_INET, SOCK_STREAM)
tcpSocket.bind(ADDR)
# set the max number of tcp connection
tcpSocket.listen(5)

print('waiting for connection...')
clientSocket, clientAddr = tcpSocket.accept()
print('conneted form: %s' % clientAddr[0])

while True:
    print("begin...")
    data = clientSocket.recv(6)
    img_size = data
    print("图片的大小为：", int(img_size))

    if len(data) > 0:
        # 接收json的size
        data = clientSocket.recv(4)
        json_size = data
        print("json的长度为：", int(json_size))

        # 接收json内容
        tempSize = 0
        data = clientSocket.recv(int(json_size))
        json_data = json.loads(data)
        # name = json_data['name']
        f = open("/Users/kk/PycharmProjects/flask_socket/json.json", "w")
        j = json.dumps(json_data)
        f.write(j)

        f.close()

        # 接收图片
        curSize = 0
        new_filename = os.path.join('/Users/kk/PycharmProjects/flask_socket', 'temp_face.jpg')
        fp = open(new_filename, 'wb')
        print('start receiving...')
        while curSize < int(img_size):
            if int(img_size) - curSize > 1024:
                data = clientSocket.recv(1024)
                curSize += len(data)
            else:
                data = clientSocket.recv(int(img_size) - curSize)
                curSize = int(img_size)
            fp.write(data)
        fp.close()
        print('over...')
    else:
        print('close')
        break


tcpSocket.close()