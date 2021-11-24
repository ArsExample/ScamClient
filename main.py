import socket

ip = input("enter server ip")
print(ip)

sock = socket.socket()
sock.connect(("localhost", 2345))

commandExit = False

while not commandExit:
    s = input()
    if s != "exit":
        sock.send(s.encode("utf-8"))
    else:
        print("Terminating the process")
        commandExit = True
        break

    data = str(sock.recv(1024))[2:-1]
    print(data)
if commandExit:
    print("Successfully terminated by client")
sock.close()