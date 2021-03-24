# Client编写步骤
# 1. 创建socket
# 2. 建立连接
# 3. 使用send和recv方法进行通信

# 一个简单的客户端实现
import socket

address=("127.0.0.1", 5000)
# 客户端：发送一个数据，再接收一个数据
# 1. 创建一个socket: 声明socket类型，同时生成链接对象
tcp_c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 建立连接
try:
    print(f"尝试与服务器进行连接...")
    tcp_c.connect(address)
except Exception:
    print("连接错误...")

while True:
    # 3. 先发送一条消息
    client_Data=input("请输入：")
    tcp_c.send(client_Data.encode('utf-8')) # 发送数据
    # 4. 再接收一条消息
    data=tcp_c.recv(1024)
    data = data.decode('utf-8')
    print(f'从服务器接收到的数据是：{data}')

# 5. 关闭连接
tcp_c.close()

# Conclusion：
# 1. 客户端能够使用一个TCP套接字向服务器发送数据之前，必须在客户端与服务器之间创建一个TCP连接
# 2. clientScoket.connect(serverName, sever.Port): 执行三次握手，创建TCP连接
# 3. clientSocket.close(): 关闭客户端和服务器之间的连接
# 4. connectScoket.close(): 向客户端发送完毕之后关闭该连接套字
# TCP需要两个套接字，UDP只要一个
# TCP服务器支持n个并行连接，每条连接来自不同客户端，TCP连接需要n+1个套接字即可。