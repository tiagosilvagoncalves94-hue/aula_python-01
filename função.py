def mostra_menu():
    print("=====MENU RESTARANTE====")
    print("1 - VER O CARDAPIO")
    print("2 - FAZER PEDIDO")
    print("3 - VER CONTA")
    print("4  -  SAIR")

while True:
    mostra_menu()
    opção = input("escolha uma opção: ")
    match opção:
        case "1": 
            print("-----cardapio-----")
            print("pizza - $35")
            print("hambuger - $35")
            print("refrigerante - $10")
        case "2": 
            print("o que deseja pedir? ")
            print("pizza - $35")
            print("hambuger - $35")
            print("refrigerante - $10")
            pedido = int(input("escolha: "))

            match pedido:
                case 1:
                    conta = 0
                    conta += 20
                    print("pedido selecionado : pizza")
                case 2:
                    conta = 0
                    conta += 20
                    print("pedido selecionado : hamburguer")
                case 3:
                    conta = 0
                    conta += 10
                    print("pedido selecionado : refrigenate")
                case _:
                    print("opção invalida")    
        case "3": 
            print(f"\no valor da sua conta : r$ {conta}") 
        case "4": 
            print("obrigado por nos visitar") 
            break
        case _:
            print("volte ao menu")