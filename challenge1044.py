a, b = map(int, input().split())

numbers = [a, b]

if a % b == 0 or b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")