from Seq0 import seq_count
from Seq0 import seq_read_fasta
list_of_sequences = ["U5", "ADA", "FRAT1", "FXN"]
for e in list_of_sequences:
    filename = "Sequences/" + e + ".txt"
    seq = seq_read_fasta(filename)
    print("Gene", e + ":", seq_count(seq))
