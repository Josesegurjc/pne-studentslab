from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.100.113" # your IP address
PORT = 8081

c = Client(IP, PORT)
print(c)

print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")

