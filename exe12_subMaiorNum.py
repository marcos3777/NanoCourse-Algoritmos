num1 = int (input("Digite um número: "))
num2 = int (input("Digite outro número: "))
num3 = int (input("Digite outro número: "))

def subMenor(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1 - num2
    elif num2 > num1 and num2 > num3:
        return num2 - num3
    else:
        return num3 - num1
    
total = subMenor(num1, num2, num3)
print(f"O maior número é {total}")