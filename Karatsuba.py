# n - степень двойки
def Karatsuba(x, y, n):
    if n == 1:
        return x * y
    else:
        a, b = x // 10 ** (n // 2), x % 10 ** (n // 2)
        c, d = y // 10 ** (n // 2), y % 10 ** (n // 2)
        p = a + b
        q = c + d
        ab = Karatsuba(a, c, n // 2)
        cd = Karatsuba(b, d, n // 2)
        pq = Karatsuba(p, q, n // 2)
        print(pq)
        return 10 ** n * Karatsuba(a, c, n // 2) + 10 ** (n // 2) * (pq - ab - cd) + Karatsuba(b, d, n // 2)

x, y, n = map(int, input().split())
print(f"Recursive multiplication: {Karatsuba(x, y, n)}")
print(f"Multiplication: {x * y}")
