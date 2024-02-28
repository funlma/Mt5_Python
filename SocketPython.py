import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind(("192.168.1.3", 8888))
serversocket.listen(10)

connection, addr = serversocket.accept()
print("[INFO]\tConnexion etablie:", addr)

msg = "\0"
while not "END CONNECTION\0" in msg and msg != "":
    msg = connection.recv(1024).decode()
    print("[INFO]\tMenssage:", msg)
connection.close()
serversocket.close()