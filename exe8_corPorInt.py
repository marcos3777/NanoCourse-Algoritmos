from unittest import case

'''dados dois numeros, imprima se ambos forem positivos, se ambos forem impares ou diferentes nos demais casos'''

num1 = int (input("Digite um número: "))
num2 = int (input("Digite outro número: "))

match num1 > 0 and num2 > 0:
    case True:
        print("Ambos são positivos")
    case False:
        match num1 % 2 != 0 and num2 % 2 != 0:
            case True:
                print("Ambos são ímpares")
            case False:
                print("Diferentes")