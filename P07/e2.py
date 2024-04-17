list_of_genes = ["FRAT1", "ADA", "FXN", "RNU6_269P", "MIR633", "TTTY4C", "RBMY2YP", "FGFR3", "KDR", "ANK2"]
list_of_identifiers = ["ENSG00000165879", "ENSG00000196839", "ENSG00000165060", "ENSG00000212379", "ENSG00000207552", "ENSG00000228296", "ENSG00000227633", "ENSG00000068078", "ENSG00000128052", "ENSG00000145362"]
dict1 = dict(zip(list_of_genes, list_of_identifiers))
print("Dictionary of Genes!")
print("There are", len(dict1), "genes in the dictionary:")
for e in dict1:
    print(e + ":", "--->", dict1[e])
