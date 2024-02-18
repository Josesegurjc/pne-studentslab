from Seq0 import seq_read_fasta
filename = "U5"
print("DNA file:", filename)
print("The first 20 bases are:")
string = seq_read_fasta(filename)
print(string[:20])
