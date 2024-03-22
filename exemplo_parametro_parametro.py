# passagem de parametros entre funcoes por referencia

def trocarComReferencia(x, y):
    z = x
    x = y
    y = z
    return x, y

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
trocarComReferencia(a, b)
print(a)
print(b)