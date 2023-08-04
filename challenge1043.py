a, b, c = map(float, input().split())

soma_ab = a + b
soma_ac = a + c
soma_bc = b + c

if (a < soma_bc and b < soma_ac and c < soma_ab):
    perimetro = a + b + c
    print("Perimetro = {0:.1f}".format(perimetro))
else:
    area = ((a + b) * c)/2
    print("Area = {0:.1f}".format(area))