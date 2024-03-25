# passagem de parametros entre funcoes por referencia

def trocarComReferencia(a, b):
    values = [a, b]
    z = values[0]
    values[0] = values[1]
    values[1] = z
    return values[0], values[1]

a = [0]
b = [0]
a[0] = int(input("Digite um número: "))
b[0] = int(input("Digite outro número: "))
a[0], b[0] = trocarComReferencia(a[0], b[0])
print(a[0])

print(b[0])