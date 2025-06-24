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

        def send_with_retry(sock, message, address, max_retries=5):
    timeout = 1.0  # 初始超时1秒
    for attempt in range(max_retries):
        try:
            sock.settimeout(timeout)
            sock.sendto(message.encode(), address)
            data, _ = sock.recvfrom(1024)
            return data.decode()
        except socket.timeout:
            print(f"Timeout (attempt {attempt + 1}), retrying...")
            timeout *= 2  # 指数退避
    return None

    print(f"Downloading {filename} [{'*' * received_chunks}]", end='\r')