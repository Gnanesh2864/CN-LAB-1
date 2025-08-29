import socket

def main():
    HOST = "0.0.0.0"      # Listen on all interfaces
    PORT = 9999           # Port > 5000
    server_name = "Server of Bhargav"   # <-- change to your name
    server_number = 42    # Pick a number between 1 and 100

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print(f"[SERVER] {server_name} listening on {HOST}:{PORT}...")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"\n[SERVER] Connection from {addr}")
                data = conn.recv(1024).decode().strip()
                if not data:
                    print("[SERVER] No data received.")
                    continue

                print(f"[SERVER] Raw message: {data}")
                parts = data.split(",")
                if len(parts) != 2:
                    print("[SERVER] Invalid format. Expected: 'ClientName,Number'")
                    continue

                client_name, client_num_str = parts
                try:
                    client_num = int(client_num_str)
                except ValueError:
                    print("[SERVER] Invalid integer from client.")
                    continue

                if not (1 <= client_num <= 100):
                    print(f"[SERVER] Invalid integer {client_num}. Closing server.")
                    return

                # Display summary
                print("\n--- Communication Summary ---")
                print(f"Client’s name    : {client_name}")
                print(f"Server’s name    : {server_name}")
                print(f"Client’s integer : {client_num}")
                print(f"Server’s integer : {server_number}")
                print(f"Sum              : {client_num + server_number}")

                # Send response back
                reply = f"{server_name},{server_number}"
                conn.sendall(reply.encode())

if __name__ == "__main__":
    main()
