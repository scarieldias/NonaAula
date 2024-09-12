# MAnipulação Dicionários/Objetos

livro = {"autor": "Alessandro", "ano": 2023, "titulo": "É melhor ser feliz do que ter razão"}

print(livro)

# Acessando Valores

adicionar = input("Quer atualizar ano de produção do livro ? Informe um ano  ")

livro["ano"] = adicionar

# Adicionando um nova chave-valor

# pessoa["cidade"] = "São Paulo"
print("Dados Atualizados", livro)