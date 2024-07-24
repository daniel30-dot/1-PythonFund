gameName = "Fifa 23"
gameDescription = """
Fifa é um jogo de Futebol, desenvolvido pela EA sports,
e que possibillita jogar online ou localmente
"""

print(gameName.upper()) # Retornar string em maiúsculo
print(gameName.lower()) # Retornar string em minúsculo
print(gameName.capitalize()) # Apenas a primeira letra em maiúsculo
print(gameName.title()) # Apenas a primeria letra em maiúsculo
print(gameName.center(10, '-')) # Retorna a string centralizada com caractere de preenchimento
print(gameName.find("a")) # Retorna uma posição de um determinado caractere
print(gameDescription.count("f")) # Conta caracteres
print(gameDescription.count("a")) # Conta caracteres
print(gameDescription.replace("Fifa", "Pes")) # Altera um elemento por outro 
print(gameDescription.split(',')) #Quebra a string, usando caractere como separador