a, b, c = input().split(" ")
d, e, f = input().split(" ")

code1, units1, price1 = int(a), int(b), float(c)
code2, units2, price2 = int(d), int(e), float(f)

total = (units1 * price1) + (units2 * price2)

print("VALOR A PAGAR: R$ %.2f" %total)