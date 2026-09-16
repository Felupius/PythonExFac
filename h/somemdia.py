val = [7.5, 8.0, 6.5, 9.0, 5.5]

soma = 0 
qnt = 0

for i in val:
    soma += i
    qnt += 1

media = soma / qnt 
print(f"Soma = {soma}, e a media e {media}")