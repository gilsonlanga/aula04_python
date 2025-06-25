# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
# Crie um dicionário para armazenar informações de um livro, incluindo título, 
# autor e ano de publicação. Imprima cada informação.

livro_01: dict = {
    "Titulo": "Game of Thrones",
    "Autor": "Estagiário",
    "Ano": 2005
}

livro_02: dict = {
    "Titulo": "Game of Thrones 2",
    "Autor": "Estagiário",
    "Ano": 2007
}

# print(livro_01)

lista_elementos: list = livro_01.items()
for elemento in lista_elementos:
    print()

lista_livros: list = []

lista_livros.append(livro_01)
lista_livros.append(livro_02)

# print(lista_livros)


lista_livros_dict:dict = {
    "livro_01": {
        "Titulo": "Game of Thrones 1",
        "Autor": "Estagiário",
        "Ano": 2005},
    
    "livro_02": {
            "Titulo": "Game of Thrones 2",
            "Autor": "Estagiário",
            "Ano": 2007
    }
}

print(lista_livros_dict["livro_01"])
print(lista_livros_dict["livro_01"]["Titulo"])

# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.