num1 = int(input(f"Digite um numero inteiro: "))
num2 = int(input(f"Digite outro numero inteiro: "))
operacao = input("Informe a operação: ")
if operacao == "+":
    print(num1 + num2)
elif operacao == "-":
    print(num1 - num2)
elif operacao == "*":
    print(num1 * num2)
elif operacao == "/":
    print(num1 / num2)
else:
    print("ERRO! Operação inexistente")