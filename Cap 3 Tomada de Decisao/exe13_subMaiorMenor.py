num1 = int (input("Digite um número: "))
num2 = int (input("Digite outro número: "))
num3 = int (input("Digite outro número: "))



def maiorMenor(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        maior = num1
        if num2 < num3:
            menor = num2
        else:
            menor = num3
    elif num2 > num1 and num2 > num3:
        maior = num2
        if num1 < num3:
            menor = num1
        else:
            menor = num3
    else:
        maior = num3
        if num1 < num2:
            menor = num1
        else:
            menor = num2
    return maior,menor

total = maiorMenor(num1, num2, num3)
print(f"{total[0]} - {total[1]} = {total[0] - total[1]}")



