num = int (input("Digite um número: "))
num2 = int (input("Digite outro número: "))

if num > num2:
    print(f"{num} - {num2} = {num - num2}") 
elif num < num2:
    print(f"{num2} - {num} = {num2 - num}")
else:
    print(f"{num} - {num2} = 0")
