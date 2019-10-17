import socket
from socket import*
import sys
import webbrowser
import os

ip = sys.argv[1]
port = sys.argv[2]
filename = sys.argv[3]

hostname = gethostbyaddr(ip)[0]
adderess = (hostname, int(port))

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((adderess))

request = "GET /" + filename + " HTTP/1.1\r"
#print(request)
clientSocket.send(request.encode("utf-8"))
full_msg = ""
while 1:
    msg = clientSocket.recv(1000)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")
print(full_msg)
f = open("D:\\Python Codes\\HTTPServer\\new.html", "w+", encoding="utf-8")
for i in range(0, len(full_msg)):
    f.write(full_msg[i])

webbrowser.open("D:\\Python Codes\\HTTPServer\\new.html", new= 2)


clientSocket.close()
