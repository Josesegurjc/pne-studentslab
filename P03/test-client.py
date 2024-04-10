from Client0 import Client

PORT = 8085
IP = "127.0.0.1"
c = Client(IP, PORT)
print("* Testing PING...")
print(c.talk("PING"))
print("* Testing GET...")
for n in range(0, 5):
    header = "GET " + str(n) + ":"
    message = "GET " + str(n)
    print(header, c.talk(message))
sequence = c.talk("GET 0")
print("* Testing INFO...")
message = "INFO " + sequence
print(c.talk(message))
print("* Testing COMP...")
print("COMP", sequence)
message = "COMP " + sequence
print(c.talk(message))
print("* Testing REV...")
print("REV", sequence)
message = "REV " + sequence
print(c.talk(message))
print("* Testing GENE...")
list_of_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for gene in list_of_genes:
    print("GENE", gene)
    message = "GENE " + gene
    print(c.talk(message))
