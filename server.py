# import socket

# HOST = ""
# PORT = 8084

# address = (HOST,PORT)

# connection = 0
# sock = socket.create_server(address, family=socket.AF_INET)

# while connection < 1:
#     sock.listen()

from threading import Thread
a = 0
def prints():
    global a
    while True:
        a= 2+a
t = Thread(target=prints)
g = Thread(target=prints)
b = Thread(target=prints)
t.run()
g.run()
b.run()