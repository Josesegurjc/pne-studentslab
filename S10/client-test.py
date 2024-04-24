from Client0 import Client
from termcolor import colored
PORT = 8080
IP = "127.0.0.1"
c1 = Client(IP, PORT)
for i in range(0, 5):
    string0 = "Message " + str(i)
    string1 = c1.talk(string0)
    print("To Server:", colored(string0, "blue"))
    print("From Server:", colored(string1, "green"))
