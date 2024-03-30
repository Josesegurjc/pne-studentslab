from Client0 import Client

IP = "127.0.0.1"
PORT = 8085

c1 = Client(IP, PORT)
resp = c1.talk("info/A")
print(resp)