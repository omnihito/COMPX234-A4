import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 51234))
    print("Server started on port 51234")

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received from {addr}: {data.decode()}")

if __name__ == "__main__":
    main()

    import threading

def handle_file_transfer(filename, client_addr):
    transfer_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    transfer_port = random.randint(50000, 51000)
    transfer_socket.bind(('localhost', transfer_port))
    
    # 发送OK响应
    response = f"OK {filename} SIZE 1234 PORT {transfer_port}"
    # ...实际文件传输逻辑...

def main():
    while True:
        data, addr = server_socket.recvfrom(1024)
        if data.decode().startswith("DOWNLOAD"):
            threading.Thread(
                target=handle_file_transfer,
                args=(data.decode().split()[1], addr)
            ).start()