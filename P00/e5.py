from Seq0 import seq_count
from Seq0 import seq_read_fasta
list_of_sequences = ["U5", "ADA", "FRAT1", "FXN"]
for e in list_of_sequences:
    seq = seq_read_fasta(e)
    print("Gene", e, ":", seq_count(seq))
