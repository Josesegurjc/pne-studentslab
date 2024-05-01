import http.server
import http.client
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
import json
from Seq1 import Seq



def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

def get_ensembl_info(ENDPOINT):
    SERVER = 'rest.ensembl.org'
    PARAMS = "?content-type=application/json"
    if ENDPOINT.find("?") != -1:
        PARAMS = PARAMS[1:]
    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)

    # -- Send the request message, using the GET method. We are
    # -- requesting the main page (/)
    try:
        conn.request("GET", ENDPOINT + PARAMS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    response = list((r1.status, json.loads(data1)))
    return response


# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open the form1.html file
        # Read the index from the file

        url_path = urlparse(self.path)
        path = url_path.path  # we get it from here
        arguments = parse_qs(url_path.query)

        if path == "/":
            contents = Path("html/index.html").read_text()
        elif path == "/listSpecies":
            response = get_ensembl_info("info/species")
            list_of_species = response[1]["species"]
            try:
                limit = arguments["limit"][0]
            except KeyError:
                limit = str(len(list_of_species))
            text1 = "The total number of species in the ensembl is: " + limit
            text2 = "The limit you have selected is: " + limit
            text3 = "<ul>"
            for e in list_of_species[0: int(limit)]:
                text3 += "<li>" + e["common_name"]
            text3 += "</ul>"
            contents = read_html_file("limit.html").render(context={"todisplay": text1, "todisplay2": text2, "todisplay3": text3})
        elif path == "/karyotype":
            species = arguments["species"][0]
            endpoint = "/info/assembly/" + species
            response = get_ensembl_info(endpoint)
            if response[0] == 200:
                list_of_chromosomes = response[1]["karyotype"]
                text1 = "<ul>"
                for e in list_of_chromosomes:
                    text1 += "<li>" + e
                text1 += "</ul>"
                contents = read_html_file("karyotype.html").render(context={"todisplay": text1})
            else:
                contents = Path("html/error.html").read_text()
        elif path == "/chromosomeLength":
            species = arguments["species"][0]
            chromo = arguments["chromosome"][0]
            endpoint = "/info/assembly/" + species
            response = get_ensembl_info(endpoint)
            if response[0] == 200:
                list1 = response[1]["top_level_region"]
                text1 = "The length of the chromosome is: "
                for e in list1:
                    if e["name"] == chromo:
                        text1 += str(e["length"])
                contents = read_html_file("chromosome_length.html").render(context={"todisplay": text1})
            else:
                contents = Path("html/error.html").read_text()
        elif path == "/geneSeq":
            gene = arguments["gene"][0]
            endpoint1 = "/xrefs/symbol/human/" + gene
            id = get_ensembl_info(endpoint1)
            if id[0] == 200:
                endpoint2 = "/sequence/id/" + id[1][0]["id"]
                response = get_ensembl_info(endpoint2)
                sequence = response[1]["seq"]
                sequence1 = ""
                j = 0
                for i in range(0, len(sequence), 50):
                    sequence1 += "<p>" + sequence[j:i] + "</p>"
                    j = i
                contents = read_html_file("geneseq.html").render(context={"todisplay": sequence1})
            else:
                contents = Path("html/error.html").read_text()
        elif path == "/geneInfo":
            gene = arguments["gene"][0]
            endpoint1 = "/xrefs/symbol/human/" + gene
            response = get_ensembl_info(endpoint1)
            if response[0] == 200:
                id = response[1][0]["id"]
                endpoint2 = "/sequence/id/" + id
                response2 = get_ensembl_info(endpoint2)
                sequence = response2[1]["seq"]
                length = len(sequence)
                chromosome = response2[1]["desc"].split(":")[2]
                text = "<p>The gene starts with " + sequence[0] + "</p>"
                text += "<p>The gene ends with " + sequence[-1] + "</p>"
                text += "<p>The total length of the gene is " + str(length)
                text += "<p> The id of the gene is " + id
                text += "<p> This gene can be found in the chromosome " + chromosome + "</p>"
                contents = read_html_file("genecalc.html").render(context={"todisplay": text})
        elif path == "/geneCalc":
            gene = arguments["gene"][0]
            endpoint1 = "/xrefs/symbol/human/" + gene
            id = get_ensembl_info(endpoint1)
            if id[0] == 200:
                endpoint2 = "/sequence/id/" + id[1][0]["id"]
                response = get_ensembl_info(endpoint2)
                sequence = Seq(response[1]["seq"])
                length = sequence.len(sequence.strbases)
                text = "<p>The total length of the gene is " + str(length) + "</p>"
                bases_count = sequence.seq_count(sequence.strbases)
                for e in bases_count:
                    text += "<p>" + e + ":" + str(round(((bases_count[e] / length) * 100), 2)) + "%"
                contents = read_html_file("genecalc.html").render(context={"todisplay": text})
        elif path == "/geneList":
            chromo = arguments["chromo"][0]
            end = arguments["end"][0]
            try:
                start = arguments["start"][0]
            except KeyError:
                start = 0
            start = 1000000
            end = 2000000
            endpoint = "/overlap/region/human/" + chromo + ":" + str(start) + "-" + str(end) + "?feature=gene;"
            print(endpoint)
            response = get_ensembl_info(endpoint)
            if response[0] == 200:
                text1 = "<ul>"
                list_of_names = []
                i = 0
                for e in response[1]:
                    if "external_name" in e.keys():
                        list_of_names.append(e["external_name"])
                for e in list_of_names:
                    text1 += "<li>" + e
                text1 += "</ul>"
                contents = read_html_file("genelist.html").render(context={"todisplay": text1})
        else:
            contents = Path("html/error.html").read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(str.encode(contents))))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
