def classificar_nota(nota):
    if nota >= 7:
        return "Aprovado com destaque"
    elif nota >= 5 :
        return "Aprovado"
    else:
        return "reprovado"