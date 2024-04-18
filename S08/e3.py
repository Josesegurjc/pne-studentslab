import socket

# SERVER IP, PORT
PORT = 8080
IP = "192.168.100.113"
# depends on the computer the server is running

while True:
    # -- Ask the user for the message
    message = str(input("Enter your message"))
    # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # -- Establish the connection to the Server
    s.connect((IP, PORT))
    # -- Send the user message
    s.send(message.encode())
    # -- Close the socket
    s.close()
