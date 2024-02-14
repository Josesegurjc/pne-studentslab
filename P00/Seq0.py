def seq_ping():
    print("OK")


def seq_read_fasta(filename):
    from pathlib import Path
    file_info = Path(filename).read_text()
    file_info = file_info[file_info.index("\n"):]
    file_info = file_info.replace("\n", "")
    return file_info


def seq_len(seq):
    from pathlib import Path
    filename = seq + ".txt"
    file_info = Path(filename).read_text()
    file_info = file_info[file_info.index("\n"):]
    file_info = file_info.replace("\n", "")
    length = len(file_info)
    print("Gene", seq, "->", "Length:", length)


def seq_count_base(seq, base):
    from pathlib import Path
    filename = seq + ".txt"
    file_info = Path(filename).read_text()
    file_info = file_info[file_info.index("\n"):]
    file_info = file_info.replace("\n", "")
    count = 0
    for e in file_info:
        if e == base:
            count += 1
    return count


def seq_count(seq):
    keys = ["A", "T", "C", "G"]
    values = []
    from Seq0 import seq_count_base
    for e in keys:
        count = seq_count_base(seq, e)
        values.append(count)
    dict1 = dict(zip(keys, values))
    return dict1


def seq_reverse(seq, n):
    from pathlib import Path
    filename = seq + ".txt"
    file_info = Path(filename).read_text()
    file_info = file_info[file_info.index("\n"):]
    file_info = file_info.replace("\n", "")
    file_info = file_info[:n]
    reverse_string = ""
    for i in range(0, len(file_info)):
        reverse_string += file_info[-i]
    return reverse_string


def seq_complement(seq):
    from pathlib import Path
    filename = seq + ".txt"
    file_info = Path(filename).read_text()
    file_info = file_info[file_info.index("\n"):]
    file_info = file_info.replace("\n", "")
    complement = ""
    for e in file_info:
        if e == "A":
            complement += "T"
        if e == "T":
            complement += "A"
        if e == "C":
            complement += "G"
        if e == "G":
            complement += "C"
    return complement


def most_frecuent_base(seq):
    from pathlib import Path
    filename = seq + ".txt"
    file_info = Path(filename).read_text()
    file_info = file_info[file_info.index("\n"):]
    file_info = file_info.replace("\n", "")
    values = ["A", "T", "G", "C"]
    count_a = file_info.count("A")
    count_t = file_info.count("T")
    count_g = file_info.count("G")
    count_c = file_info.count("C")
    keys = [count_a, count_t, count_g, count_c]
    dict1 = dict(zip(keys, values))
    maximum = max(count_a, count_c, count_t, count_g)
    base = dict1[maximum]
    return base
