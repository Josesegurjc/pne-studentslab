with open("dna.txt", "r") as f:
    countA = 0
    countC = 0
    countG = 0
    countT = 0
    general_count = 0
    for sequence in f:
        for e in sequence:
            general_count += 1
            if e == "A":
                countA += 1
            if e == "C":
                countC += 1
            if e == "G":
                countG += 1
            if e == "T":
                countT += 1
print("Total number of bases:", general_count)
print("A:", countA)
print("C:", countC)
print("T:", countT)
print("G:", countG)
