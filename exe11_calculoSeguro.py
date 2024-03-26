from unittest import case

idade = int (input("Digite a idade: "))
risco = input("Digite o risco (\"B\" para \"baixo risco\", \"M\" para \"médio risco\" e \"A\" para \"alto risco\"):")

match risco:
    case "B":
        if idade > 17 and idade < 20:
            print("1")
        if idade >= 21 and idade < 24:
            print("2")
        if idade >= 25 and idade < 34:
            print("3")
        if idade >= 35 and idade < 64:
            print("4")
        if idade >= 65 and idade < 70:
            print("7")
    case "M":
        if idade > 17 and idade < 20:
            print("2")
        if idade >= 21 and idade < 24:
            print("3")
        if idade >= 25 and idade < 34:
            print("4")
        if idade >= 35 and idade < 64:
            print("5")
        if idade >= 65 and idade < 70:
            print("8")
    case "A":
        if idade > 17 and idade < 20:
            print("3")
        if idade >= 21 and idade < 24:
            print("4")
        if idade >= 25 and idade < 34:
            print("5")
        if idade >= 35 and idade < 64:
            print("6")
        if idade >= 65 and idade < 70:
            print("9")



