from Seq0 import seq_count_base
list_of_sequences = ["U5", "ADA", "FRAT1", "FXN"]
list_of_bases = ["A", "C", "T", "G"]
for e in list_of_sequences:
    print("Gene", e, ":")
    for c in list_of_bases:
        print(c, ":", seq_count_base(e, c))
