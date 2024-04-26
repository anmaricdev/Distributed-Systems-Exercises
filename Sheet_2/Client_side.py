import socket
import signal
import sys
import threading

def sigint_handler(signal, frame):
    print("\nClient shutting down...")
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

def handle_server(server_socket):
    while True:
        data = server_socket.recv(1024)
        if data:
            message = data.decode('utf-8')
            print(f"Server said: {message}")
        else:
            print("Server disconnected.")
            break

    server_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('localhost', 1337))

    server_thread = threading.Thread(target=handle_server, args=(server_socket,))
    server_thread.start()
    print("Connection with Server established. Feel free to send a message to the server.")

    while True:
        message = input()
        if message:
            server_socket.sendall(message.encode('utf-8'))

if __name__ == "__main__":
    main()