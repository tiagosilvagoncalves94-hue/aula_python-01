#dicionario
jogador = {}

for i in range(5):
   nome = input("Qual o nome do jogador :") #chave
   pontos = input("Qual quantidade de pontos conquistados:") #valor

   jogador[nome] = pontos

for jogador[nome], pontos in jogador.items():
   print(f"{jogador[nome]} | {pontos}")
if nome in jogador:
   print("jogador encontrado")
else: 
   print("jogador não encontrado.")

for jogador[nome], pontos in jogador.items():
   print(f"{jogador[nome]} | {pontos}")


   
   
  
   
