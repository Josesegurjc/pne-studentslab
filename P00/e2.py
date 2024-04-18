from Seq0 import seq_read_fasta
filename = "U5.txt"
folder = "Sequences/"
full_filename = folder + filename
print("DNA file:", filename)
print("The first 20 bases are:")
string = seq_read_fasta(full_filename)
print(string[:20])
