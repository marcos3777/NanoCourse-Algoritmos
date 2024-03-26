'''escreva em python: algoritmo "Exercicio_Fixação_k"

var

   taxa: inteiro;
   tres: inteiro;
   cinco: inteiro;

inicio

   escreva("Informe a taxa cobrada pelo correio: ")
   leia(taxa)

   se (taxa MOD 5 = 0) ENTÃO
      cinco := INT(taxa / 5)
   SENÃO

      se (taxa MOD 5 = 1) ENTÃO
         cinco := INT((taxa - 6) / 5)
         tres := 2
      SENÃO

         se (taxa MOD 5 = 2) ENTÃO
            cinco := INT((taxa - 12) / 5)
            tres := 4
         SENÃO

            se (taxa MOD 5 = 3) ENTÃO
               cinco := INT((taxa - 3) / 5)
               tres := 1
            SENÃO

               se (taxa MOD 5 = 4) ENTÃO
                  cinco := INT((taxa - 9) / 5)
                  tres := 3
               fimse
            fimse
         fimse
      fimse
   fimse

   escreval ("Para enviar a carta é preciso: ")
   escreval (cinco, " selos de cinco centavos ")
   escreval (tres, " selos de tres centavos ")

fimalgoritmo '''


taxa = int(input("Informe a taxa cobrada pelo correio: "))
if taxa % 5 == 0:
    cinco = int(taxa / 5)
    tres = 0
else:
    if taxa % 5 == 1:
        cinco = int((taxa - 6) / 5)
        tres = 2
    else:
        if taxa % 5 == 2:
            cinco = int((taxa - 12) / 5)
            tres = 4
        else:
            if taxa % 5 == 3:
                cinco = int((taxa - 3) / 5)
                tres = 1
            else:
                if taxa % 5 == 4:
                    cinco = int((taxa - 9) / 5)
                    tres = 3
print("Para enviar a carta é preciso: ")
print(cinco, "selos de cinco centavos")
print(tres, "selos de tres centavos")

