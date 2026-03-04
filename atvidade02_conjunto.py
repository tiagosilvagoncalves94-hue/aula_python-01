thiago = {"chuteira" , "meia" , "blusa", "garrafa","short"}
gerson = {"tenis" , "meia" , "calça de goleiro", "luva de goleiro","mochila"}
davi = {"boné" , "bola adidas" , "suplemento", "relógio","cone de treino"}
matheus = {"copo" , "blusa de frio" , "raquete", "blusa","creatina"}

comun = thiago.intersection(gerson|davi|matheus)
print(comun)

total = thiago.union(gerson|davi|matheus)
print(total)
print(len(total))



