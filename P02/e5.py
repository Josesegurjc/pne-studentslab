from Client0 import Client
from Seq1 import Seq


PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"  # your IP address
PORT = 8080

c = Client(IP, PORT)
print(c)
gene = "Sequences/FRAT1"
s = Seq()
s = str(s.seq_read_fasta(gene))
print("Gene FRAT1:", s)
c.talk("Sending FRAT1 Gene to the server, in fragments of 10 bases...")
i = 0
j = 10
for n in range(1, 6):
    string = "Fragment " + str(n) + ": "
    sequence = s[i: j]
    message = string + sequence
    i = j
    j += 10
    print(message)
    c.talk(message)
