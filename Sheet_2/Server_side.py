import socket
import signal
import sys
import threading
import datetime

def sigint_handler(signal, frame):
    print("Server shutting down...")
    print("------------------------------------------------------------------------------")
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

def handle_client(client_socket, client_address):
    print("------------------------------------------------------------------------------")
    print(f"Connection established with {client_address}.\nWaiting on input...")
    print("------------------------------------------------------------------------------")
    
    while True:
        data = client_socket.recv(1024)
        if data:
            message = data.decode('utf-8')
            print(f"Client said: {message}")
        else:
            print("------------------------------------------------------------------------------")
            print(f"Client {client_address} disconnected.")
            break

    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 1337))
server_socket.listen(1)
print("------------------------------------------------------------------------------")
print("Server listening on port 1337...")
print("------------------------------------------------------------------------------")

client_socket, client_address = server_socket.accept()

client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
client_thread.start()

while True:
    message = input()
    if message:
        client_socket.sendall(message.encode('utf-8'))