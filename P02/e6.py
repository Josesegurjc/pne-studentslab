from Client0 import Client
from Seq1 import Seq


PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.100.113" # your IP address
PORT = 8080

c1 = Client(IP, PORT)
print(c1)
c2 = Client(IP, 8081)
print(c2)
gene = "Sequences/FRAT1"
s = Seq()
s = str(s.seq_read_fasta(gene))
print("Gene FRAT1:", s)
c1.talk("Sending FRAT1 Gene to the server, in fragments of 10 bases...")
c2.talk("Sending FRAT1 Gene to the server, in fragments of 10 bases...")
i = 0
j = 10
for n in range(1, 11):
    string = "Fragment " + str(n) + ": "
    sequence = s[i: j]
    message = string + sequence
    i = j
    j += 10
    print(message)
    if n % 2 == 0:
        c2.talk(message)
    else:
        c1.talk(message)