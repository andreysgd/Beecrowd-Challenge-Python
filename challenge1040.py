n1, n2, n3, n4 = map(float, input().split())

average = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print("Media: %.1f" % average)

if average >= 7.0:
    print("Aluno aprovado.")
elif average < 5.0:
    print("Aluno reprovado.")
elif 5 <= average <= 6.9:
    print("Aluno em exame.")
    newScore = float(input())
    print("Nota do exame: %.1f" % newScore)
    newAverage = (newScore + average) / 2
    if newAverage >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % newAverage)
