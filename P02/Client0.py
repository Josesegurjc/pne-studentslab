class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print("OK")

    def __str__(self):
        string = "Connection to SERVER at " + str(self.ip) + ", PORT: " + str(self.port)
        return string

    def talk(self, msg):
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.send(str.encode(msg))
        response = s.recv(2048).decode("utf-8")
        s.close()
        return response

