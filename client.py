import socket

HOST = "127.0.0.1"   # Change to server IP if on another machine
PORT = 5001

client_name = "Client of R. Gnanesh"   # <-- Change to your name
client_number = int(input("Enter an integer (1–100): "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = f"{client_name},{client_number}"
    s.sendall(message.encode())

    data = s.recv(1024).decode()
    server_name, server_number = data.split(",")
    server_number = int(server_number)

    print(f"[CLIENT] Client Name: {client_name}")
    print(f"[CLIENT] Server Name: {server_name}")
    print(f"[CLIENT] Client Number: {client_number}")
    print(f"[CLIENT] Server Number: {server_number}")
    print(f"[CLIENT] Sum = {client_number + server_number}")
