import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 51234)
    
    message = "PING"
    client_socket.sendto(message.encode(), server_address)
    print(f"Sent: {message}")

    data, _ = client_socket.recvfrom(1024)
    print(f"Received: {data.decode()}")

if __name__ == "__main__":
    main()