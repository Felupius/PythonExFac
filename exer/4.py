Maioridade = True
doc = True
moradorLocal = False

if Maioridade and doc:
    print(f"Pode se inscrever")

elif not Maioridade and moradorLocal:
    print(f"Pode se inscrever")

else:
    print(f"Não pode se inscrever")
