from unittest import case

num1 = int (input("Digite um número: "))
num2 = int (input("Digite outro número: "))
num3 = int (input("Digite outro número: "))
maior,meio,menor = 0

match num1>num2 and num1>num3:
    case True:
        maior = num1
        match num2>num3:
            case True:
                meio = num2
                menor = num3
            case False: 
                meio = num3
                menor = num2
    case False:
        match num2>num1 and num2>num3:
            case True:
                maior = num2
                match num1 > num3:
                    case True:
                        meio = num1
                        menor = num3
                    case False:

        #finalizar

