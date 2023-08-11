import socket
import settings as settings

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((settings.address, settings.port))

server.listen(4)

while True:
    client, address = server.accept()

    print("user connected.")
    client.send("connected.".encode("utf-8"))

    data = client.recv(1024).decode("utf-8")
    print(data)
