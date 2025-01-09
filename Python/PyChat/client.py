import socket

host, port = ('localhost', 5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    socket.connect((host, port))
    while True:
        cmd = input("> ")
        data = cmd.encode("utf8")
        socket.sendall(data)
        reception = socket.recv(1024)
        reception = reception.decode("utf8")
        if cmd=="disconnect":
            socket.close()
            quit()

except:
    print("Erreur")
finally:
    socket.close()