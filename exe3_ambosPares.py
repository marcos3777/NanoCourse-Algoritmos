num = int (input("Digite um número: "))
num2 = int (input("Digite outro número: "))

if num % 2 == 0 and num2 % 2 == 0:
    print("Ambos Pares")
elif num % 2 != 0 and num2 % 2 != 0:
    print("Ambos Ímpares")
else:
    print("Demais Casos")

    
    