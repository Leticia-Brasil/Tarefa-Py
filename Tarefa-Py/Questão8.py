temp = int(input(f"Digite a temperatura em graus Celsius: "))
if temp > 30:
    print("Calor!")
elif temp >= 15 and temp <= 30:
    print("Temperatura normal!")
else:
    print("Frio!")