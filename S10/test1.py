from Client0 import Client
PORT = 8081
IP = "127.0.0.1"
c1 = Client(IP, PORT)
string1 = c1.talk("Test1...")
print(string1)
c2 = Client(IP, PORT)
string2 = c2.talk("Test2...")
print(string2)
c3 = Client(IP, PORT)
string3 = c3.talk("Test3...")
print(string3)