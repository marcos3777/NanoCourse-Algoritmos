from unittest import case
def Fator(idade):
    if idade > 17 and idade < 20:
        return 1
    if idade >= 21 and idade < 24:
        return 2
    if idade >= 25 and idade < 34:
        return 3
    if idade >= 35 and idade < 64:
        return 4
    if idade >= 65 and idade < 70:
        return 7

idade = int (input("Digite a idade: "))
sexo = input("Digite o sexo: ")
mensalidade = int (input("Digite a mensalidade: "))
fator = Fator(idade)

match sexo:
    case "M":
        valorFinal = mensalidade * fator
        print(valorFinal)
    case "F":
        valorFinal = mensalidade * fator * 0.8
        print(valorFinal)
    case _:
        print("Sexo inválido")

    