num = int (input("Digite um número: "))
num2 = int (input("Digite outro número: "))

if num >= 0 and num2 >= 0:
    print("Verde")
elif num < 0 and num2 < 0:
    print("Vermelho")
else:
    print("Amarelo")
