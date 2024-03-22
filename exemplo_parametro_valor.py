# passagem de parametros entre funcoes por valor
def trocarComValores(x, y):
    z = x
    x = y
    y = z

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
trocarComValores(a, b)
print(a)
print(b)
