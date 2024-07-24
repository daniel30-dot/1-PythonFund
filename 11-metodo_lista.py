gamesList = ["Fifa 23", "Star Wars", "The Legend of Zelda", "Read Dead 2"]

# 1 - Tamanho da lista
print(len(gamesList))

# 2 - Recupera um item da lista pelo índice
print(gamesList.index("Star Wars"))

# 3 - Adiciona um item ao final de uma lista
gamesList.append("Gta V")
print(gamesList)

# 4- Ordena lista
gamesList.sort()
print(gamesList)

# 5 - Copia os itens de uma lista para outra
gamesReset = gamesList.copy()
gamesReset.remove('Fifa 23')
gamesReset.remove('Star Wars')
print(gamesReset)

# 6 - Remove todos os itens de uma lista

gamesList.clear()
print(gamesList)