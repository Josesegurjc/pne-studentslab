def fibosum(n):
    n1 = 0
    n2 = 1
    sum = 1
    for i in range(0, n - 1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        sum += n3
    print("Sum of the First", n, "terms of the Fibonacci series:", sum)


fibosum(5)
fibosum(10)
