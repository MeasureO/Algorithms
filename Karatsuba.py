# n - степень двойки
def Karatsuba(x, y, n):
    if n == 1:
        return x * y
    else:
        a, b = x // 10 ** (n // 2), x % 10 ** (n // 2)
        c, d = y // 10 ** (n // 2), y % 10 ** (n // 2)
        ac = Karatsuba(a, c, n // 2)
        bd = Karatsuba(b, d, n // 2)
        ab_cd = Karatsuba(a + b, c + d, n // 2)
        return 10 ** n * ac + 10 ** (n // 2) * (ab_cd - ac - bd) + bd

x, y, n = map(int, input().split())
print(f"Recursive multiplication: {Karatsuba(x, y, n)}")
print(f"Multiplication: {x * y}")
