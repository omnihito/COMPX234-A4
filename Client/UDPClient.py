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

    def process_file_list(file_path):
    try:
        with open(file_path) as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        return []