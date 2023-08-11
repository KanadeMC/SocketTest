import socket
import clientsettings

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((clientsettings.address, 5555))

while True:
    data = client.recv(1024)
    print(data.decode("utf-8"))

    client.send(input().encode("utf-8"))
