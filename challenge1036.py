a, b, c = map(float, input().split())

calDelta = ((b ** 2) - (4 * a * c))
delta = calDelta ** (1 / 2)

if a <= 0 or calDelta < 0.0:
    print("Impossivel calcular")
else:
    R1 = (-b + delta) / (2 * a)
    R2 = (-b - delta) / (2 * a)

    print("R1 = {0:.5f}".format(R1))
    print("R2 = {0:.5f}".format(R2))
