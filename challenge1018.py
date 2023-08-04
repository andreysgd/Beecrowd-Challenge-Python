value = int(input())

hundred = value // 100
rest1 = value - (100 * hundred)

fifty = rest1 // 50
rest2 = rest1 - (50 * fifty)

twenty = rest2 // 20
rest3 = rest2 - (20 * twenty)

ten = rest3 // 10
rest4 = rest3 - (10 * ten)

five = rest4 // 5
rest5 = rest4 - (5 * five)

two = rest5 // 2
rest6 = rest5 - (2 * two)

one = rest6 // 1
rest7 = rest6 - (1 * one)

# print("100", hundred, rest1)
# print("50", fifty, rest2)
# print("20", twenty, rest3)
# print("10", ten, rest4)
# print("5", five, rest5)
# print("2", two, rest6)
# print("1", one, rest7)

print(value)
print("%i nota(s) de R$ 100,00" % hundred)
print("%i nota(s) de R$ 50,00" % fifty)
print("%i nota(s) de R$ 20,00" % twenty)
print("%i nota(s) de R$ 10,00" % ten)
print("%i nota(s) de R$ 5,00" % five)
print("%i nota(s) de R$ 2,00" % two)
print("%i nota(s) de R$ 1,00" % one)
