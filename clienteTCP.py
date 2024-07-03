import socket
import threading






class Client:

    host = '127.0.0.1'
    port = 5000
    nick = ''


    def receive_message(self, client):
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if(message == 'NICK'):
                    client.send(self.nick.encode('utf-8'))
                else:
                    print(message)
            except:
                break


    def send_message(self, client):
        while True: 
            message = input()
            if(message == "disc"):
                client.send(message.encode('utf-8'))
                client.close()
                break
            else:
                client.send(f'{self.nick} disse: {message}'.encode('utf-8'))

            



def main():
    chatter = Client()
    chatter.nick = input("Escreva seu nick: ")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (chatter.host, chatter.port)
    client.connect(dest)

    t1 = threading.Thread(target=chatter.receive_message, args=(client,))
    t2 = threading.Thread(target=chatter.send_message, args=(client,))

    t1.start()
    t2.start()



if __name__ == "__main__":
    main()




