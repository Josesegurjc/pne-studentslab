import requests

# Specify the chromosome name or ID
chromosome = "9"  # Change this to the desired chromosome
start_position = 0  # Specify the start position of the region
end_position = 5700000  # Specify the end position of the region

# Construct the Ensembl API endpoint
ensembl_api_url = f"http://rest.ensembl.org/overlap/region/human/{chromosome}:{start_position}-{end_position}?feature=gene;content-type=application/json"

# Initialize an empty list to store gene names
gene_names = []

# Make a GET request to retrieve gene data
response = requests.get(ensembl_api_url)

# Check if the request was successful
if response.ok:
    # Parse the JSON response
    gene_data = response.json()

    # Extract gene names from the response
    for gene in gene_data:
        if gene['biotype'] == 'protein_coding':
            gene_names.append(gene['external_name'])

    # Print the list of gene names
    print("Genes in chromosome", chromosome, "region", start_position, "-", end_position, ":", gene_names)
else:
    print("Failed to retrieve gene data. Status code:", response.status_code)
