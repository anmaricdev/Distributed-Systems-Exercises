import socket
import sys

def main():
    # Check if a message is provided
    if len(sys.argv) != 2:
        print("Usage: python client.py <message>")
        sys.exit(1)

    # Get the message from the command line argument
    message = sys.argv[1]

    # Create a socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 1337))

    # Send the message to the server
    client_socket.sendall(message.encode('utf-8'))

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    main()