import socket
import signal
import sys

def handle_sigint(signal, frame):
    print("\nServer shutting down...")
    sys.exit(0)

# Register the SIGINT handler
signal.signal(signal.SIGINT, handle_sigint)

# Create a socket and bind to localhost on port 1337
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 1337))
server_socket.listen(1)
print("Server listening on port 1337...")

# Keep the server running until a signal is received
while True:
    # Accept a new client connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    # Receive data from the client
    data = client_socket.recv(1024)  # Receive up to 1024 bytes
    if data:
        # Print the message on the local console
        print(f"Received message: {data.decode('utf-8')}")

    # Close the client socket
    client_socket.close()