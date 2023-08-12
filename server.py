import socket
import settings as settings
import threading


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.all_client = []
        self.server.bind((settings.address, settings.port))
        self.server.listen(4)
        print("Сервер запущен.")
        threading.Thread(target=self.process).start()

    #Обработка клиента
    def process(self):
        while True:
            client, address = self.server.accept()
            if client not in self.all_client:
                self.all_client.append
                print("Пользователь подключился.")
                client.send("Подключен.".encode("utf-8"))
                threading.Thread(target=self.message, args=(client,)).start()

    #Обработка сообщения
    def message(self, client_socket):
        while True:
            message = client_socket.recv(1024)
            print(message.decode("utf-8"))
            if message == b'exit':
                self.all_client.remove(client_socket)
                break

            for client in self.all_client:
                if client != client_socket:
                    client.send(message)


myserver = Server(settings.address, settings.port)
