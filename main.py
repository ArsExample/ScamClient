import socket

ip = input("enter server ip\n")

sock = socket.socket()
sock.connect((ip, 2345))

commandExit = False

while not commandExit:
    s = input()
    if s != "exit":
        sock.send(s.encode("utf-8"))
    elif s == "exit":
        print("Terminating the process")
        commandExit = True
        break

    data = str(sock.recv(1024))[2:-1]
    print(data)
if commandExit:
    print("Successfully terminated by client")
else:
    print("idk why it don't works")
sock.close()