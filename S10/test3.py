from Client0 import Client
PORT = 8080
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
c4 = Client(IP, PORT)
string4 = c4.talk("Test4...")
print(string4)
c5 = Client(IP, PORT)
string5 = c5.talk("Test5...")
print(string5)
