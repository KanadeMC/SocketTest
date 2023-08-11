import socket
import clientsettings as settings

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((settings.address, settings.port))

while True:
    data = client.recv(1024)
    print(data.decode("utf-8"))

    client.send(input().encode("utf-8"))
