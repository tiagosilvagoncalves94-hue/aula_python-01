menu = ()
escolha = ()
print("=======|MENU|=======")
print("Voce tem mais de 18+ anos? ")
print("1 - sim")
print("2 - não")
escolha = input("selecione uma opção:")
match escolha:
    case "1": 
        print("acesso liberado com sucesso!")     
    case "2":
        print("você não tenho 18+")
        print("acesso bloqueado!")
    case _: 
        print("ERROR |TENTE NOVAMENTE|")

