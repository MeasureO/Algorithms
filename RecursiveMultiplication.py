# n - степень двойки
def RecIntMult(x, y, n):
    if n == 1:
        return x * y
    else:
        a, b = x // 10 ** (n // 2), x % 10 ** (n // 2)
        c, d = y // 10 ** (n // 2), y % 10 ** (n // 2)
        return 10 ** n * RecIntMult(a, c, n // 2) + 10 ** (n // 2) * (RecIntMult(a, d, n // 2) + RecIntMult(b, c, n // 2)) + RecIntMult(b, d, n // 2)

x, y, n = map(int, input().split())
print(f"Recursive multiplication: {RecIntMult(x, y, n)}")
print(f"Multiplication: {x * y}")
