import socket
import termcolor
from pathlib import Path


# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.split('\n')

    # -- The request line is the first
    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")
    # -- Generate the response message
    # It has the following lines
    # Status line
    # header
    # blank line
    # Body (content to send)

    # This new contents are written in HTML language
    infoA = Path("html/info/A.html").read_text()
    infoC = Path("html/info/C.html").read_text()
    infoG = Path("html/info/G.html").read_text()
    infoT = Path("html/info/T.html").read_text()

    status_line = "HTTP/1.1 200 OK\n"

    # -- Add the Content-Type header
    header = "Content-Type: text/html\n"

    # -- Build the message by joining together all the parts
    if req_line.find("/info/A") != -1:
        header += f"Content-Length: {len(infoA)}\n"
        response_msg1 = status_line + header + "\n" + infoA
        cs.send(response_msg1.encode())
    elif req_line.find("/info/C") != -1:
        header += f"Content-Length: {len(infoC)}\n"
        response_msg1 = status_line + header + "\n" + infoC
        cs.send(response_msg1.encode())
    elif req_line.find("/info/G") != -1:
        header += f"Content-Length: {len(infoG)}\n"
        response_msg1 = status_line + header + "\n" + infoG
        cs.send(response_msg1.encode())
    elif req_line.find("/info/T") != -1:
        header += f"Content-Length: {len(infoT)}\n"
        response_msg1 = status_line + header + "\n" + infoT
        cs.send(response_msg1.encode())
    else:
        response_msg1 = status_line + header + "\n"
        cs.send(response_msg1.encode())




# -------------- MAIN PROGRAM
# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
ls.bind((IP, PORT))

# -- Become a listening socket
ls.listen()

print("Server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped!")
        ls.close()
        exit()
    else:

        # Service the client
        process_client(cs)

        # -- Close the socket
        cs.close()