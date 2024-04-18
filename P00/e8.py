from Seq0 import most_common_base
from Seq0 import seq_read_fasta
list_of_sequences = ["U5", "ADA", "FRAT1", "FXN"]
for e in list_of_sequences:
    filename = "Sequences/" + e + ".txt"
    string = seq_read_fasta(filename)
    base = most_common_base(string)
    print("Gene", e + ":", "Most frequent base:", base)
