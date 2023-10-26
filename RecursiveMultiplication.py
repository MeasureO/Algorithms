def RecIntMult(x, y):
    if x < 10 and y < 10:
            return x * y
    m = max(len(str(x)), len(str(y)))
    n = m // 2
    a, b = x // 10 ** n, x % 10 ** n
    c, d = y // 10 ** n, y % 10 ** n
    ac = RecIntMult(a, c)
    bd = RecIntMult(b, d)
    return 10 ** (2 * n) * ac + 10 ** n * (RecIntMult(a, d) + RecIntMult(b, c)) + bd

x, y = map(int, input().split())
print(f"Recursive multiplication: {RecIntMult(x, y)}")
print(f"Multiplication: {x * y}")
