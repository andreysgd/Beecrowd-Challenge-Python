a, b, c = map(float, input().split(" "))
pi = 3.14159

areaRectangleTriangle = (a * c)/ 2
areaCircle = pi * (c ** 2)
areaTrapezium = ((a + b) * c )/ 2
areaSquare = b ** 2
areaRectangle = a * b

print("TRIANGULO: %.3f" % areaRectangleTriangle)
print("CIRCULO: %.3f" % areaCircle)
print("TRAPEZIO: %.3f" % areaTrapezium)
print("QUADRADO: %.3f" % areaSquare)
print("RETANGULO: %.3f" % areaRectangle)
