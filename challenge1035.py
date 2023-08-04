a, b, c, d = map(int, input().split())

sumCD = c + d
sumAB = a + b

if b > c and d > a and sumCD > sumAB and c > 0 and d > 0 and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")