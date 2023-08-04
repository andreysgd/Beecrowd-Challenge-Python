code, quant = map(int, input().split())

if code == 1:
    valor = quant * 4.00
    print("Total: R$ {0:.2f}".format(valor))
elif code == 2:
    valor = quant * 4.50
    print("Total: R$ {0:.2f}".format(valor))
elif code == 3:
    valor = quant * 5.00
    print("Total: R$ {0:.2f}".format(valor))
elif code == 4:
    valor = quant * 2.00
    print("Total: R$ {0:.2f}".format(valor))
elif code == 5:
    valor = quant * 1.50
    print("Total: R$ {0:.2f}".format(valor))
