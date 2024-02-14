from Seq0 import most_frecuent_base
list_of_sequences = ["U5", "ADA", "FRAT1", "FXN"]
for e in list_of_sequences:
    base = most_frecuent_base(e)
    print("Gene", e, ":", "Most Frecuent base:", base)