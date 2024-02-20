class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases=None):
        self.strbases = strbases
        condition = True
        if strbases is None:
            print("NULL sequence created!")
        else:
            correct_letters = "ACGT"
            for e in strbases:
                if not(e in correct_letters):
                    condition = False
            if condition:
                print("New sequence created!")
            else:
                print("INVALID sequence!")

    def __str__(self):
        string = self.strbases
        if string is None:
            string = "NULL"
        else:
            correct_letters = "ACGT"
            condition = True
            for e in string:
                if not (e in correct_letters):
                    condition = False
            if not condition:
                string = "ERROR"
        return string

    def len(self, strbases=None):
        self.strbases = strbases
        if strbases is None:
            length = 0
        else:
            correct_letters = "ACGT"
            condition = True
            for e in strbases:
                if not (e in correct_letters):
                    condition = False
            if not condition:
                length = 0
            else:
                length = len(strbases)
        return length

    def seq_count_base(self, base):
        count = 0
        for e in self.strbases:
            if e == base:
                count += 1
        return count

    def seq_count(self, strbases=None):
        self.strbases = strbases
        keys = ["A", "T", "C", "G"]
        values = [0, 0, 0, 0]
        if strbases is None:
            dict1 = dict(zip(keys, values))
        else:
            values = []
            from Seq0 import seq_count_base
            for e in keys:
                count = seq_count_base(self.strbases, e)
                values.append(count)
            dict1 = dict(zip(keys, values))
        return dict1

    def seq_reverse(self, strbases=None):
        self.strbases = strbases
        if strbases is None:
            reverse_string = "NULL"
        else:
            correct_letters = "ACGT"
            condition = True
            for e in strbases:
                if not (e in correct_letters):
                    condition = False
            if not condition:
                reverse_string = "ERROR"
            else:
                reverse_string = ""
                for i in range(1, len(strbases)):
                    reverse_string += strbases[-i]
                reverse_string += strbases[0]
        return reverse_string

    def seq_complement(self, strbases=None):
        self.strbases = strbases
        if strbases is None:
            complement = "NULL"
        else:
            correct_letters = "ACGT"
            condition = True
            for e in strbases:
                if not (e in correct_letters):
                    condition = False
            if not condition:
                complement = "ERROR"
            else:
                complement = ""
                for e in strbases:
                    if e == "A":
                        complement += "T"
                    if e == "T":
                        complement += "A"
                    if e == "C":
                        complement += "G"
                    if e == "G":
                        complement += "C"
        return complement

    def seq_read_fasta(self, filename):
        from pathlib import Path
        filename = filename + ".txt"
        file_info = Path(filename).read_text()
        file_info = file_info[file_info.index("\n"):]
        file_info = file_info.replace("\n", "")
        self.strbases = file_info
        return self

    def most_common_base(self, strbases):
        self.strbases = strbases
        values = ["A", "T", "G", "C"]
        count_a = strbases.count("A")
        count_t = strbases.count("T")
        count_g = strbases.count("G")
        count_c = strbases.count("C")
        keys = [count_a, count_t, count_g, count_c]
        dict1 = dict(zip(keys, values))
        maximum = max(count_a, count_c, count_t, count_g)
        base = dict1[maximum]
        return base


class Gene(Seq):
    def __init__(self, strbases, name=""):
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        return self.name + "-" + self.strbases
    pass
