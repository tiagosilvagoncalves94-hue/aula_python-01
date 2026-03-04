workshop1 = {"gerson" , "davi" , "matheus" , "alisson" , "enzo" , "gerson"}
workshop2 = {"luiz" , "isack" , "gabriel" , "samuel" , "douglas" , "luiz"}

participante_a = set (workshop1) 
participante_b = set (workshop2) 

print(f"participantes do evento 1: {participante_a}")
print(f"participantes do evento 2: {participante_b}")

todos_participantes = participante_a.union(participante_b)
print(f"total de parcipantes: {todos_participantes}\n")
print(len(todos_participantes))

ambos_worshops = participante_a.intersection(participante_b) 

so_a = participante_a.difference(participante_b)
print(f"apenas parcipantes do Workshop1 : {so_a}")
