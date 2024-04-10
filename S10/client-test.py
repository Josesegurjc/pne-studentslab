from Client0 import Client
PORT = 8083
IP = "127.0.0.1"
c1 = Client(IP, PORT)
for i in range(0, 5):
    string0 = "Message " + str(i)
    string1 = c1.talk(string0)
    print("To Server:", string0)
    print("From Server:", string1)
