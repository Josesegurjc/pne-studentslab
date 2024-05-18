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


def get_ensembl_info(endpoint):
    server = 'rest.ensembl.org'
    params = "?content-type=application/json"
    if endpoint.find("?") != -1:
        params = params[1:]
    conn = http.client.HTTPConnection(server)
    try:
        conn.request("GET", endpoint + params)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
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
    list_of_chromosomes = []
    if response[0] == 200:
        list_of_chromosomes = response[1]["karyotype"]
    return list_of_chromosomes


def get_chromosome_length(arguments):
    species = arguments["species"][0]
    chromo = arguments["chromosome"][0]
    endpoint = "/info/assembly/" + species
    response = get_ensembl_info(endpoint)
    length = ""
    if response[0] == 200:
        list1 = response[1]["top_level_region"]
        for e in list1:
            if e["name"] == chromo:
                length = str(e["length"])
    return length


def get_gene_seq(arguments):
    gene = arguments["gene"][0]
    endpoint1 = "/xrefs/symbol/human/" + gene
    identification = get_ensembl_info(endpoint1)
    sequence = ""
    if identification[1]:
        endpoint2 = "/sequence/id/" + identification[1][0]["id"]
        response = get_ensembl_info(endpoint2)
        sequence = response[1]["seq"]
    return sequence


def get_gene_info(arguments):
    gene = arguments["gene"][0]
    endpoint1 = "/xrefs/symbol/human/" + gene
    response = get_ensembl_info(endpoint1)
    list1 = []
    if response[1]:
        identification = response[1][0]["id"]
        endpoint2 = "/sequence/id/" + identification
        response2 = get_ensembl_info(endpoint2)
        sequence = response2[1]["seq"]
        length = len(sequence)
        chromosome = response2[1]["desc"].split(":")[2]
        list1 = [chromosome, sequence, length, identification]
    return list1


def get_gene_calc(arguments):
    gene = arguments["gene"][0]
    endpoint1 = "/xrefs/symbol/human/" + gene
    identification = get_ensembl_info(endpoint1)
    list1 = []
    if identification[1]:
        endpoint2 = "/sequence/id/" + identification[1][0]["id"]
        response = get_ensembl_info(endpoint2)
        sequence = Seq(response[1]["seq"])
        length = sequence.len(sequence.strbases)
        bases_count = sequence.seq_count(sequence.strbases)
        list1 = [length, bases_count]
    return list1


def get_gene_list(arguments):
    chromo = arguments["chromo"][0]
    end = arguments["end"][0]
    list_of_names = []
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
    return list_of_names


socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        content_type = "text/html"
        json_condition = False
        contents = Path("html/error.html").read_text()

        if "json" in arguments.keys():
            if arguments["json"][0] == "1":
                content_type = "application/json"
                json_condition = True
                response = {"Error": "Path not recognized"}
        if path == "/":
            if json_condition:
                response = {"message": "Welcome to the server"}
                contents = json.dumps(response)
            else:
                contents = Path("html/index.html").read_text()
        elif path == "/listSpecies":
            list_of_species, limit = get_list_species(arguments)
            if limit.isdigit():
                if int(limit) >= 0:
                    if not json_condition:
                        text1 = "The total number of species in the ensembl is: " + str(len(list_of_species))
                        if len(list_of_species) < int(limit):
                            text2 = "The limit chosen is higher than the total amount of species, then all species are shown"
                        else:
                            text2 = "The limit you have selected is: " + limit
                        text3 = "<ul>"
                        for species in list_of_species[0: int(limit)]:
                            text3 += "<li>" + species["common_name"]
                        text3 += "</ul>"
                        contents = read_html_file("limit.html").render(context={"todisplay": text1, "todisplay2": text2, "todisplay3": text3})
                    else:
                        list_of_names = []
                        for species in list_of_species[:int(limit)]:
                            list_of_names.append(species["common_name"])
                        response = {
                            "total_species": len(list_of_species),
                            "limit": int(limit),
                            "species": list_of_names
                        }
        elif path == "/karyotype":
            list_of_chromosomes = get_karyotype(arguments)
            if list_of_chromosomes:
                if not json_condition:
                    text1 = "The name of the chromosomes are:"
                    text2 = "<ul>"
                    for e in list_of_chromosomes:
                        text2 += "<li>" + e
                    text2 += "</ul>"
                    contents = read_html_file("karyotype.html").render(context={"todisplay": text1, "todisplay2": text2})
                elif json_condition:
                    response = {"karyotype": list_of_chromosomes}
        elif path == "/chromosomeLength":
            length = get_chromosome_length(arguments)
            if length:
                if not json_condition:
                    contents = read_html_file("chromosome_length.html").render(context={"todisplay": length})
                else:
                    response = {"Chromosome Length": length}
        elif path == "/geneSeq":
            sequence = get_gene_seq(arguments)
            if sequence:
                if not json_condition:
                    sequence1 = ""
                    k = 0
                    for i in range(0, len(sequence), 50):
                        sequence1 += "<p>" + sequence[k:i] + "</p>"
                        k = i
                    contents = read_html_file("geneseq.html").render(context={"todisplay": sequence1})
                else:
                    response = {"Sequence": sequence}
        elif path == "/geneInfo":
            list1 = get_gene_info(arguments)
            if list1:
                sequence = list1[1]
                chromosome = list1[0]
                length = list1[2]
                identification = list1[3]
                if not json_condition:
                    text = "<p>The gene starts with " + sequence[0] + "</p>"
                    text += "<p>The gene ends with " + sequence[-1] + "</p>"
                    text += "<p>The total length of the gene is " + str(length)
                    text += "<p> The id of the gene is " + identification
                    text += "<p> This gene can be found in the chromosome " + chromosome + "</p>"
                    contents = read_html_file("genecalc.html").render(context={"todisplay": text})
                else:
                    response = {
                        "Start": sequence[0],
                        "End": sequence[-1],
                        "Length": length,
                        "ID": identification,
                        "Chromosome": chromosome
                    }
        elif path == "/geneCalc":
            list1 = get_gene_calc(arguments)
            if list1:
                length = list1[0]
                bases_count = list1[1]
                if not json_condition:
                    text = "<p>The total length of the gene is " + str(length) + "</p>"
                    for e in bases_count:
                        text += "<p>" + e + ":" + str(round(((bases_count[e] / length) * 100), 2)) + "%"
                    contents = read_html_file("genecalc.html").render(context={"todisplay": text})
                else:
                    response = {
                        "Length": length,
                        "A": (str(round(((bases_count["A"] / length) * 100), 2)) + "%"),
                        "T": (str(round(((bases_count["T"] / length) * 100), 2)) + "%"),
                        "C": (str(round(((bases_count["C"] / length) * 100), 2)) + "%"),
                        "G": (str(round(((bases_count["G"] / length) * 100), 2)) + "%"),
                    }
        elif path == "/geneList":
            list_of_names = get_gene_list(arguments)
            if list_of_names:
                if not json_condition:
                    if list_of_names:
                        text1 = "<ul>"
                        for e in list_of_names:
                            text1 += "<li>" + e
                        text1 += "</ul>"
                    else:
                        text1 = "There are no genes in the chosen limits"
                    contents = read_html_file("genelist.html").render(context={"todisplay": text1})
                else:
                    if list_of_names:
                        response = {"List": list_of_names}
                    else:
                        response = {"List": " "}

        if json_condition:
            contents = json.dumps(response)

        self.send_response(200)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))

        return


# Setup and run the server
Handler = TestHandler
PORT = 8091

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
