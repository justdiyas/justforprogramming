import socket
from colorama import Fore

HOST = socket.gethostbyname(socket.gethostname())
PORT = 2222
ADDRESS = (HOST, PORT)
FORMAT = 'UTF-8'

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDRESS)
    server.listen()
    print(f'Server is listening on [{HOST}]')
    conn, addr = server.accept()
    print(f'[NEW CONNECTION] {addr} is connected.')
    connected = True
    while connected:
        conn.send(f'{Fore.RED}[WARNING]{Fore.RESET} Server can receive and send up to 128 bytes of data.'.encode(FORMAT))
        message = conn.recv(128).decode(FORMAT)
        if message == 'disconnect':
            connected = False
        print(message)
    conn.close()

start_server()