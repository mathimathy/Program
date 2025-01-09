import socket
import threading

class ThreadForClient(threading.Thread):
    def __init__(self, conn,id):
        threading.Thread.__init__(self)
        self.conn=conn
        self.id=id
        print(f"Le client {self.id} vient de se connecter")
    
    def run(self):
        data = self.receive()
        print(f"{self.id}: {data}")
        if data=="disconnect":
            self.disconnect()

    def disconnect(self):
        self.conn.close()
        print(f"Le client {self.id} a été déconnecté")
            
    
    def receive(self):
        data = self.conn.recv(1024)
        data = data.decode("utf8")
        return data
    
    def send(self, msg):
        msg = msg.encode('utf8')
        self.conn.sendall(msg)

#-------------------------------
host, port = ('', 5566)
clients=[]

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host,port))
print("Le serveur est connecté")

while True:
    socket.listen(5)
    conn, address = socket.accept()
    
    clients.append(ThreadForClient(conn, len(clients)))
    clients[-1].start()

socket.close()