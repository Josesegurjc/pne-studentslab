def fibosum(n):
    n1 = 0
    n2 = 1
    suma = 1
    for i in range(0, n - 1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        suma += n3
    print("Sum of the First", n, "terms of the Fibonacci series:", suma)


fibosum(5)
fibosum(10)
