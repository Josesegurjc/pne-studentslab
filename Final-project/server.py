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

def get_list_species(arguments):
    response = get_ensembl_info("info/species")
    list_of_species = response[1]["species"]
    try:
        limit = arguments["limit"][0]
    except KeyError:
        limit = str(len(list_of_species))
    return list_of_species, limit

def get_karyotype(arguments):
    species = arguments["species"][0]
    endpoint = "/info/assembly/" + species
    response = get_ensembl_info(endpoint)
    if response[0] == 200:
        list_of_chromosomes = response[1]["karyotype"]
    else:
        list_of_chromosomes = []
    return list_of_chromosomes

def get_chromosome_length(arguments):
    species = arguments["species"][0]
    chromo = arguments["chromo"][0]
    endpoint = "/info/assembly/" + species
    response = get_ensembl_info(endpoint)
    if response[0] == 200:
        list1 = response[1]["top_level_region"]
        text1 = "The length of the chromosome is: "
        for e in list1:
            if e["name"] == chromo:
                text1 += str(e["length"])
    else:
        text1 = ""
    return text1


def get_gene_seq(arguments):
    gene = arguments["gene"][0]
    endpoint1 = "/xrefs/symbol/human/" + gene
    id = get_ensembl_info(endpoint1)
    if id[0] == 200:
        endpoint2 = "/sequence/id/" + id[1][0]["id"]
        response = get_ensembl_info(endpoint2)
        sequence = response[1]["seq"]
    else:
        sequence = ""
    return sequence


def get_gene_info(arguments):
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
        list1 = [chromosome, sequence, length, id]
    else:
        list1 = []
    return list1

def get_gene_calc(arguments):
    gene = arguments["gene"][0]
    endpoint1 = "/xrefs/symbol/human/" + gene
    id = get_ensembl_info(endpoint1)
    if id[0] == 200:
        endpoint2 = "/sequence/id/" + id[1][0]["id"]
        response = get_ensembl_info(endpoint2)
        sequence = Seq(response[1]["seq"])
        length = sequence.len(sequence.strbases)
        bases_count = sequence.seq_count(sequence.strbases)
        list1 = [length, bases_count]
    else:
        list1 = []
    return list1

def get_gene_list(arguments):
    chromo = arguments["chromo"][0]
    end = arguments["end"][0]
    try:
        start = arguments["start"][0]
    except KeyError:
        start = 0
    endpoint = "/overlap/region/human/" + chromo + ":" + str(start) + "-" + str(end) + "?feature=gene;"
    response = get_ensembl_info(endpoint)
    if response[0] == 200:
        list_of_names = []
        for e in response[1]:
            if "external_name" in e.keys():
                list_of_names.append(e["external_name"])
    else:
        list_of_names = []
    return list_of_names




# Define the Server's port
PORT = 8099


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
        content_type = "text/html"
        contents = Path("html/error.html").read_text()

        if "json" in arguments.keys():
            if arguments["json"][0] == "1":
                content_type = "application/json"
                if path == "/":
                    contents = Path("html/index.html").read_text()
                elif path == "/listSpecies":
                    list1 = get_list_species(arguments)[0]
                    list_of_species = list1[0]
                    limit = list1[1]
                    text1 = "The total number of species in the ensembl is: " + str(len(list_of_species))
                    text2 = "The limit you have selected is: " + limit
                    text3 = "<ul>"
                    for e in list_of_species[0: int(limit)]:
                        text3 += "<li>" + e["common_name"]
                    text3 += "</ul>"
                    contents = read_html_file("limit.html").render(context={"todisplay": text1, "todisplay2": text2, "todisplay3": text3})
                elif path == "/karyotype":
                    list_of_chromosomes = get_karyotype(arguments)
                    if list_of_chromosomes != []:
                        text1 = "<ul>"
                        for e in list_of_chromosomes:
                            text1 += "<li>" + e
                        text1 += "</ul>"
                        contents = read_html_file("karyotype.html").render(context={"todisplay": text1})
                elif path == "/chromosomeLength":
                    length = get_chromosome_length(arguments)
                    if length != "":
                        contents = read_html_file("chromosome_length.html").render(context={"todisplay": length})
                elif path == "/geneSeq":
                    sequence = get_gene_seq(arguments)
                    if sequence != "":
                        sequence1 = ""
                        j = 0
                        for i in range(0, len(sequence), 50):
                            sequence1 += "<p>" + sequence[j:i] + "</p>"
                            j = i
                        contents = read_html_file("geneseq.html").render(context={"todisplay": sequence1})
                elif path == "/geneInfo":
                    list1 = get_gene_info(arguments)
                    if list1 != []:
                        sequence = list1[1]
                        chromosome = list1[0]
                        length = list1[2]
                        id = list1[3]
                        text = "<p>The gene starts with " + sequence[0] + "</p>"
                        text += "<p>The gene ends with " + sequence[-1] + "</p>"
                        text += "<p>The total length of the gene is " + str(length)
                        text += "<p> The id of the gene is " + id
                        text += "<p> This gene can be found in the chromosome " + chromosome + "</p>"
                        contents = read_html_file("genecalc.html").render(context={"todisplay": text})
                elif path == "/geneCalc":
                    list1 = get_gene_calc(arguments)
                    if list1 != []:
                        length = list1[0]
                        bases_count = list1[1]
                        text = "<p>The total length of the gene is " + str(length) + "</p>"
                        for e in bases_count:
                            text += "<p>" + e + ":" + str(round(((bases_count[e] / length) * 100), 2)) + "%"
                        contents = read_html_file("genecalc.html").render(context={"todisplay": text})
                elif path == "/geneList":
                    list_of_names = get_gene_list(arguments)
                    if list_of_names != []:
                        text1 = "<ul>"
                        for e in list_of_names:
                            text1 += "<li>" + e
                        text1 += "</ul>"
                        contents = read_html_file("genelist.html").render(context={"todisplay": text1})
        else:
            if path == "/":
                contents = Path("html/index.html").read_text()
            elif path == "/listSpecies":
                list1 = get_list_species(arguments)
                list_of_species = list1[0]
                limit = list1[1]
                text1 = "The total number of species in the ensembl is: " + str(len(list_of_species))
                text2 = "The limit you have selected is: " + limit
                text3 = "<ul>"
                for e in list_of_species[0: int(limit)]:
                    text3 += "<li>" + e["common_name"]
                text3 += "</ul>"
                contents = read_html_file("limit.html").render(context={"todisplay": text1, "todisplay2": text2, "todisplay3": text3})
            elif path == "/karyotype":
                list_of_chromosomes = get_karyotype(arguments)
                if list_of_chromosomes != []:
                    text1 = "<ul>"
                    for e in list_of_chromosomes:
                        text1 += "<li>" + e
                    text1 += "</ul>"
                    contents = read_html_file("karyotype.html").render(context={"todisplay": text1})
            elif path == "/chromosomeLength":
                length = get_chromosome_length(arguments)
                if length != "":
                    contents = read_html_file("chromosome_length.html").render(context={"todisplay": length})
            elif path == "/geneSeq":
                sequence = get_gene_seq(arguments)
                if sequence != "":
                    sequence1 = ""
                    j = 0
                    for i in range(0, len(sequence), 50):
                        sequence1 += "<p>" + sequence[j:i] + "</p>"
                        j = i
                    contents = read_html_file("geneseq.html").render(context={"todisplay": sequence1})
            elif path == "/geneInfo":
                list1 = get_gene_info(arguments)
                if list1 != []:
                    sequence = list1[1]
                    chromosome = list1[0]
                    length = list1[2]
                    id = list1[3]
                    text = "<p>The gene starts with " + sequence[0] + "</p>"
                    text += "<p>The gene ends with " + sequence[-1] + "</p>"
                    text += "<p>The total length of the gene is " + str(length)
                    text += "<p> The id of the gene is " + id
                    text += "<p> This gene can be found in the chromosome " + chromosome + "</p>"
                    contents = read_html_file("genecalc.html").render(context={"todisplay": text})
            elif path == "/geneCalc":
                list1 = get_gene_calc(arguments)
                if list1 != []:
                    length = list1[0]
                    bases_count = list1[1]
                    text = "<p>The total length of the gene is " + str(length) + "</p>"
                    for e in bases_count:
                        text += "<p>" + e + ":" + str(round(((bases_count[e] / length) * 100), 2)) + "%"
                    contents = read_html_file("genecalc.html").render(context={"todisplay": text})
            elif path == "/geneList":
                list_of_names = get_gene_list(arguments)
                if list_of_names != []:
                    text1 = "<ul>"
                    for e in list_of_names:
                        text1 += "<li>" + e
                    text1 += "</ul>"
                    contents = read_html_file("genelist.html").render(context={"todisplay": text1})

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', content_type)
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
