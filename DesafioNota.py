# Manipulação Dicionários/Objetos

dados = {"Alessandro" : 8 , "Elthon" : 10}

aluno = input("Digite o nome do aluno : ")

if aluno in dados:

    print(f"A nota de {aluno} é {dados[aluno]}")
else:
    print("Aluno não existe")
