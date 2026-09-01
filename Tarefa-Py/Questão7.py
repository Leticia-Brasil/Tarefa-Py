nota = float(input("Digite a sua nota: "))
if nota >= 7:
    print("Aprovado!")
elif nota >= 5 and nota <= 6.9:
    print("Recuperação!")
else:
    print("Reprovado!")