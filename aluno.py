#criação do dicionário
aluno = {}
#entrada de dados
aluno["nome"] = input("digite o nome do aluno: ")
aluno["sobrenome"] = input("digite o sobrenome do aluno: ")
aluno["idade"] = input("digite o idade do aluno: ")
aluno["curso"] = input("digite o curso do aluno: ")

#saida de dados
print(f"O nome do aluno e: {aluno["nome"]}")
print(f"O sobrenome do aluno e: {aluno["sobrenome"]}")
print(f"A idade do aluno e: {aluno["idade"]}")
print(f"O curso do aluno e: {aluno["curso"]}")