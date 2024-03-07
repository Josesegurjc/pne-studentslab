from Seq1 import Seq
import socket

# Configure the Server's IP and PORT
PORT = 8085
IP = "127.0.0.1"  # this IP address is local, so only requests from the same machine are possible

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()
list_of_sequences = ["ACGTT", "TGCA", "TAGC", "AGTC", "TCAG"]

print("SEQ server configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients!")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listening socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("A client has connected to the server!")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-readable string
        msg = msg_raw.decode()

        if msg.startswith("PING"):
            response = "OK!\n"
            print("PING command!")
            print(response)
            cs.send(response.encode())
        elif msg.startswith("GET"):
            print("GET")
            index = int(msg[msg.find(" "):])
            sequence = list_of_sequences[index]
            print(sequence)
            cs.send(sequence.encode())
        elif msg.startswith("INFO"):
            print("INFO")
            sequence = Seq(msg[msg.find(" ") + 1:])
            list_of_info = []
            list_of_info.append(str(sequence))
            list_of_info.append(sequence.len(sequence.strbases))
            list_of_info.append(sequence.seq_count(sequence.strbases))
            cs.send(str(list_of_info).encode())
        elif msg.startswith("COMP"):
            print("COMP")
            sequence = Seq(msg[msg.find(" ") + 1:])
            response = sequence.seq_complement(sequence.strbases)
            cs.send(response.encode())
            print(response)
        elif msg.startswith("REV"):
            print("REV")
            sequence = Seq(msg[msg.find(" ") + 1:])
            response = sequence.seq_reverse(sequence.strbases)
            cs.send(response.encode())
            print(response)
        elif msg.startswith("GENE"):
            print("GENE")
            gene = Seq()
            filename = "Sequences/" + msg[msg.find(" ") + 1:]
            info = gene.seq_read_fasta(filename)
            cs.send(str(info).encode())
            print(info)

        # -- Close the data socket
        cs.close()
