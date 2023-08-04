value = 576.73
# value = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for i in range(len(notas)):
    quant = 0
    while value - notas[i] >= 0:
        quant += 1
        value -= notas[i]
    print("%d nota(s) de R$ %.2f" % (quant, notas[i]))

print("MOEDAS:")
for i in range(len(moedas)):
    quant = 0
    while value - moedas[i] >= 0:
        quant += 1
        value = float(format(round(value - moedas[i], 2)))
    print("%d moeda(s) de R$ %.2f" % (quant, moedas[i]))