# Server编写步骤
# 1. 创建socket对象 --- 调用socket.socket()函数构造
# 2. 将socket绑定到指定地址
# 3. 使用socket套接字的listen方法接收连接请求
# 4. 服务器套接字通过socket的accept方法等待客户请求一个连接
# 5. 处理阶段：服务器和客户端通过send和recv方法通信--传输数据

# 一个简单的实现
import socket

# 服务器的端口和地址
address=("127.0.0.1",5000)

# 1. 创建socket
tcp_s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定端口
tcp_s.bind(address)

# 3. 监听端口
tcp_s.listen(5)         # 开始监听，表示可以使用五个链接排队

# 4. accept方法等待连接
while True:
    print(f"等待连接。。。。。。")
    conn, addr = tcp_s.accept()    # 返回客户端地址和一个新的socket连接
    print(f"接收到客客户端的{addr}")
    while True:
        # 异常处理
        try:
            # 5. 接收数据
            data=conn.recv(1024)
            print(f"接收到的数据是：{data.decode()}")
            if not data:
                break
            # 6. 发送数据
            send_Data=input("请输入：")
            conn.send(send_Data.encode())
        except ConnectionError as e:
            print(e)
        
    # 7. 关闭与客户端的连接
    conn.close()
    # 8. 关闭socket的连接
    tcp_s.close()
