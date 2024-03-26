from unittest import case


num = int (input("Escolha 1 para incluir \nEscolha 2 para excluir \nEscolha 3 para alterar \nEscolha 4 para consultar: "))
match num: 
    case 1:
        print("Incluir")
    case 2:
        print("Excluir")
    case 3:
        print("Alterar")
    case 4:
        print("Consultar")
    case _:
        print("Operação inválida")