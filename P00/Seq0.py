def seq_ping():
    print("OK")


def seq_read_fasta(filename):
    from pathlib import Path
    filename = filename + ".txt"
    file_info = Path(filename).read_text()
    file_info = file_info[file_info.index("\n"):]
    file_info = file_info.replace("\n", "")
    return file_info


def seq_len(seq):
    length = len(seq)
    return length


def seq_count_base(seq, base):
    count = 0
    for e in seq:
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
    if n is not None:
        seq = seq[:n]
    reverse_string = ""
    for i in range(1, len(seq)):
        reverse_string += seq[-i]
    reverse_string += seq[0]
    return reverse_string


def seq_complement(seq):
    complement = ""
    for e in seq:
        if e == "A":
            complement += "T"
        if e == "T":
            complement += "A"
        if e == "C":
            complement += "G"
        if e == "G":
            complement += "C"
    return complement


def most_common_base(seq):
    values = ["A", "T", "G", "C"]
    count_a = seq.count("A")
    count_t = seq.count("T")
    count_g = seq.count("G")
    count_c = seq.count("C")
    keys = [count_a, count_t, count_g, count_c]
    dict1 = dict(zip(keys, values))
    maximum = max(count_a, count_c, count_t, count_g)
    base = dict1[maximum]
    return base
