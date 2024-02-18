from Seq0 import most_common_base
from Seq0 import seq_read_fasta
list_of_sequences = ["U5", "ADA", "FRAT1", "FXN"]
for e in list_of_sequences:
    string = seq_read_fasta(e)
    base = most_common_base(string)
    print("Gene", e, ":", "Most Frecuent base:", base)
