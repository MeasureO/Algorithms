def Karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y
    m = max(len(str(x)), len(str(y)))
    n = m // 2
    a, b = x // 10 ** n, x % 10 ** n
    c, d = y // 10 ** n, y % 10 ** n
    ac = Karatsuba(a, c)
    bd = Karatsuba(b, d)
    pq = Karatsuba(a + b, c + d)
    return 10 ** (2 * n) * ac + 10 ** n * (pq - ac - bd) + bd

x, y = map(int, input().split())
print(f"Recursive multiplication: {Karatsuba(x, y)}")
print(f"Multiplication: {x * y}")
