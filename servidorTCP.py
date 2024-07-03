import socket
import threading







class Chat:

    host = '127.0.0.1'
    port = 5000
    clients = []
    nickname = []




    def receive_connection(self, server):
        while True:
            client, _ = server.accept()
            client.send("NICK".encode('utf-8'))
            nick = client.recv(1024).decode('utf-8')
            self.clients.append(client)
            self.nickname.append(nick)
            self.broadcast(f"{nick} caiu de paraquedas no bate papo!!".encode('utf-8'))
            client.send("Você foi conectado, caso queira desconexão digite 'disc' ".encode('utf-8'))

            t = threading.Thread(target=self.receive_messages, args=((client,)))
            t.start()


    def receive_messages(self, client):
        while True:
            try:
                message = client.recv(1024)
                if(message.decode('utf-8') == "disc"):
                    self.disconect_client(client)
                    continue
                self.broadcast(message)
            except:
                break            
                
    

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)


    def disconect_client(self, client):
        index = self.clients.index(client)
        self.broadcast(f"O {self.nickname[index]} saiu do bate papo da UOL!".encode('utf-8'))
        self.nickname.remove(self.nickname[index])
        self.clients.remove(client)
        client.close()


            

def main():
    chat = Chat()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (chat.host, chat.port)
    server.bind(orig)
    server.listen()
    print("Server iniciado :) ")
    chat.receive_connection(server)





if __name__ == "__main__":
    main()