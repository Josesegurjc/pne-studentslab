from termcolor import colored
import http.client
import json


PORT = 8090
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)

request = "/karyotype?species=Sumatran_orangutan3&json=1"
choice = request[:request.find("?")]

try:
    conn.request("GET", request)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")
# -- Create a variable with the data,
# -- form the JSON received
response = json.loads(data1)

if choice == "/listSpecies":
    print(colored("The total number os species in ensembl is:", "green"), response["total_species"])
    if response["total_species"] < response["limit"]:
        print(colored("The limit chosen is higher than the total amount of species, all species are shown"), "green")
    else:
        print(colored("The limit you selected is:", "green"), response["limit"])
    print(colored("The name of the species are:"))
    for species in response["species"]:
        print(species)
elif choice == "/karyotype":
    print(colored("The name of the chromosomes are:", "green"))
    for chromo in response["karyotype"]:
        print("*", chromo)
elif choice == "/chromosomeLength":
    print(colored("The total length of the selected chromosome is:", "green"), response["Chromosome Length"])
elif choice == "/geneSeq":
    print(colored("The bases of the gene are:", "green"))
    i = 0
    sequence = ""
    for base in response["Sequence"]:
        if 50 > len(response["Sequence"]):
            print(response["Sequence"])
        elif i != 50:
            sequence += base
            i += 1
        else:
            print(sequence)
            sequence = ""
            i = 0
elif choice == "/geneInfo":
    print(colored("The gene starts with", "green"), response["Start"])
    print(colored("The gene ends with", "green"), response["End"])
    print(colored("The total length of the gene is", "green"), response["Length"])
    print(colored("The id of the gene is", "green"), response["ID"])
    print(colored("This gene can be found in the chromosome", "green"), response["Chromosome"])
elif choice == "/geneCalc":
    print(colored("The total length of the gene is", "green"), response["Length"])
    for letter in ["A", "T", "C", "G"]:
        print(colored(letter + ":", "green"), response[letter])
elif choice == "/geneList":
    print(colored("The genes contained in the chromosome chosen between the start and end selected are:", "green"))
    if response["List"] != " ":
        for gene in response["List"]:
            print("*", gene)
    else:
        print("There are no genes in the chosen limits")
