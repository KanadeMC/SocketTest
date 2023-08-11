import socket
import settings

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((settings.address, 5555))

server.listen()

while True:
    user, address = server.accept()

    print("user connected.")
    user.send("connected.".encode("utf-8"))

    data = user.recv(1024)
    print(data.decode("utf-8"))
