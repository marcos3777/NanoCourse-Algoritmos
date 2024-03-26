
num1 = int (input("Digite um numero: "))
num2 = int (input("Digite outro numero: "))
num3 = int (input("Digite outro numero: "))

'''ordenar os números em ordem crescente'''

if num1 > num2 and num1 > num3:
    maior = num1
    if num2 > num3:
        meio = num2
        menor = num3
    else:
        meio = num3
        menor = num2
elif num2 > num1 and num2 > num3:
    maior = num2
    if num1 > num3:
        meio = num1
        menor = num3
    else:
        meio = num3
        menor = num1
else:
    maior = num3
    if num1 > num2:
        meio = num1
        menor = num2
    else:
        meio = num2
        menor = num1

print(f"Os números em ordem crescente são: {menor}, {meio} e {maior}")




