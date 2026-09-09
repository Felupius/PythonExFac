num = int(input("Digite um número para saber se ele é positivo, negativo ou zero e se é par ou impar:"))

if num >= 0:
    print("Positivo")

else:
    print("Negativo")


if (num % 2 == 0):
    print("PAR porque o resto é 0")
else:
    print("ÍMPAR porque o resto é 1")