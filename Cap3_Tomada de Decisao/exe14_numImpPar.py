

'''elabore um algoritmo que solicite do usuario um numero inteiro e imprima em tela? 0, caso onumero seja positivo e par, 
1, caso o numero seja positivo e impar, 2, caso o numero seja zero, 3, outros casos.'''

num = int(input("Digite um número inteiro: "))
if num == 0:
    print("2")
elif num > 0 and num % 2 == 0:
    print("0")
elif num > 0 and num % 2 != 0:
    print("1")
else:
    print("3")

