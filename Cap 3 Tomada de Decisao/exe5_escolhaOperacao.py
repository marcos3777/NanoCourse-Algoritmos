from unittest import case


num = int (input("Digite um número: "))
num2 = int (input("Digite outro número: "))
operacao = input("Digite a operação desejada: ")

match operacao:

    case "+":
        print(f"{num} + {num2} = {num + num2}")
    case "-":
        print(f"{num} - {num2} = {num - num2}")
    case "*":
        print(f"{num} * {num2} = {num * num2}")
    case "/":
        if num2 == 0:
            print("Divisão por zero")
        else:
            print(f"{num} / {num2} = {num / num2}")
    case _:
        print("Operação inválida")
#

