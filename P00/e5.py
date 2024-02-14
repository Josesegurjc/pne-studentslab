from Seq0 import seq_count
list_of_sequences = ["U5", "ADA", "FRAT1", "FXN"]
for e in list_of_sequences:
    print("Gene", e, ":", seq_count(e))
