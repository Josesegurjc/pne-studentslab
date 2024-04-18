def fibon(n):
    n1 = 0
    n2 = 1
    n3 = 0
    for i in range(0, n - 1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    print(str(n) + "th", "Fibonacci term:", n3)


fibon(5)
fibon(10)
fibon(15)
