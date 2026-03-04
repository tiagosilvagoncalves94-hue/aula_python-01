#criação 
aluno = {}
#entrada de dados
aluno["nome"] = input("digite o nome do aluno: ")
aluno["curso"] = input("digite o curso do aluno: ")
aluno["nota"] = float(input("digite a nota do aluno: "))
#saida de dados
print(f"O nome do aluno e: {aluno["nome"]}")
print(f"O curso do aluno e: {aluno["curso"]}")
print(f"Aprovado" if aluno["nota"] >= 18 else "Reprovado")
