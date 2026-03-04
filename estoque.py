#criação estoque
estoque = {
    "camisa" :50,
    "calça" :15,
    "boné" :25,
    "tenis nike" :35
}
#mostrar estoque atual
print("Estoque atual: ")
for produto, quantidade in estoque.items():
    print(f"{produto} ; {quantidade}")
#pedindo informações para usuário do sistema
nome_produto = input("\ndigite o nome do produto vendido: ")
quantidade_vendida = int(input("informe a quantidade vendida: "))
#atualização do estoque
if nome_produto in estoque:
    if quantidade_vendida <= estoque[nome_produto]:
     estoque[nome_produto] = estoque[nome_produto] - quantidade_vendida
     print("Venda realizada com sucesso!")
else:
   print("Produto não encontrado")  
#estoque atualizado
for produto , quantidade in estoque .items():
   print(f"{produto} | {quantidade}")      





