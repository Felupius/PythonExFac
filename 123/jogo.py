numS = 303
tent = 0
palpite = 0
palps = []
while(palpite != numS):
    palpite = int(input("Digite um palpite de número:"))
    palps.append(palpite)
    if palpite > 303:
        print("muito alto")
        tent +=1

    if palpite < 303:
        print("muito baixo")
        tent +=1

tent +=1 
print(f"Acerto! Tentativas: {tent}, e palpites: {palpite}")