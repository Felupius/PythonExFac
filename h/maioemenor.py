valores = [4, 17, 2, 9, 23, 1, 15]

maior = 0
menor = valores

for i in valores:
    if i > maior:
        maior = i

    if i < menor:
            menor = i

print (f"Maior: {maior}, menor: {menor}")