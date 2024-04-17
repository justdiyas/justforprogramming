import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 2222
ADDRESS = (HOST, PORT)
FORMAT = 'UTF-8'

def connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDRESS)
    connected = True
    while connected:
        print(client.recv(128).decode(FORMAT))
        message = input('Your message or "disconnect" to close connection with the server: ').encode(FORMAT)
        client.send(message)
        if message == b'disconnect':
            connected = False
    client.close()


connect_to_server()