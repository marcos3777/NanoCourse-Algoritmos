
numPar = 0
numImpar = 0
num = int(input("Digite um número: "))
testeInteiros = num % 2
if testeInteiros == 0:
    print("O número digitado é par")
    numPar = numPar + 1
else:
    print("O número digitado é ímpar")
    numImpar = numImpar + 1
num2 = int(input("Digite outro número: "))
testeInteiros = num2 % 2
if testeInteiros == 0:
    print("O número digitado é par")
    numPar = numPar + 1
else:
    print("O número digitado é ímpar")
    numImpar = numImpar + 1
num3 = int(input("Digite mais um número: "))
testeInteiros = num3 % 2
if testeInteiros == 0:
    print("O número digitado é par")
    numPar = numPar + 1
else:
    print("O número digitado é ímpar")
    numImpar = numImpar + 1

print("Dos números digitados, {} são pares e {} são ímpares".format(numPar, numImpar))


#Tambem podemos fazer da seguinte forma:

testeInteiro=0
testeInteiro = num % 2 + num2 % 2 + num3 % 2
print("Dos números digitados, {} são pares e {} são ímpares".format(3-testeInteiro, testeInteiro))



