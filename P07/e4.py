from Seq1 import Seq
import http.client
import json

gene_name = input("Write the gene name:")
list_of_genes = ["FRAT1", "ADA", "FXN", "RNU6_269P", "MIR633", "TTTY4C", "RBMY2YP", "FGFR3", "KDR", "ANK2"]
list_of_identifiers = ["ENSG00000165879", "ENSG00000196839", "ENSG00000165060", "ENSG00000212379", "ENSG00000207552", "ENSG00000228296", "ENSG00000227633", "ENSG00000068078", "ENSG00000128052", "ENSG00000145362"]
dict1 = dict(zip(list_of_genes, list_of_identifiers))

SERVER = 'rest.ensembl.org'
ENDPOINT = "/sequence/id/" + dict1[gene_name]
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

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
response = json.loads(data1)
print("Gene:", gene_name)
print("Description:", response["desc"])
bases = Seq(response["seq"])
print("Total length:", bases.len(bases.strbases))
bases_count = bases.seq_count(bases.strbases)
for e in bases_count:
    print(e + ":", bases_count[e], "(" + str(round((bases_count[e] / bases.len(bases.strbases)) * 100, 1)) + "%)")
print("Most frequent base:", bases.most_common_base(bases.strbases))



