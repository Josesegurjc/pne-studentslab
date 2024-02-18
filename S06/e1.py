class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        self.strbases = strbases
        condition = True
        correct_letters = "ACGT"
        for e in strbases:
            if not(e in correct_letters):
                condition = False
        if condition:
            print("New sequence created!")
        else:
            print("ERROR!!")

    def __str__(self):
        condition = True
        correct_letters = "ACGT"
        for e in self.strbases:
            if not (e in correct_letters):
                condition = False
        if condition:
            string = self.strbases
        else:
            string = "ERROR"
        return string

    def len(self):
        return len(self.strbases)


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
