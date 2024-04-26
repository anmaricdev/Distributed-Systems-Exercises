import socket
import signal
import sys
import threading
import datetime

def sigint_handler(signal, frame):
    print("\nServer shutting down...")
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

def handle_client(client_socket, client_address):
    print(f"Connection established with {client_address}")

    while True:
        data = client_socket.recv(1024)
        if data:
            message = data.decode('utf-8')
            print(f"Client said: {message}")
        else:
            print(f"Client {client_address} disconnected.")
            break

    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 1337))
server_socket.listen(1)
print("Server listening on port 1337...")

client_socket, client_address = server_socket.accept()

client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
client_thread.start()

while True:
    message = input()
    if message:
        client_socket.sendall(message.encode('utf-8'))