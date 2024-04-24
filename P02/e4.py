from Client0 import Client
from Seq1 import Seq
from termcolor import colored

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"  # your IP address
PORT = 8080

c = Client(IP, PORT)
print(c)
list_of_names = ["U5", "ADA", "FRAT1"]
i = 0
list2 = []
for e in list_of_names:
    filename = "Sequences/" + e
    s = Seq()
    s = str(s.seq_read_fasta(filename))
    string = "Sending " + e + " Gene to the server..."
    print("To server: ", colored(string, "blue"))
    print("From server: ", colored(c.talk(string), "green"))
    print("To server: ", colored(s, "blue"))
    print("From server: ", colored(c.talk(s), "green"))
