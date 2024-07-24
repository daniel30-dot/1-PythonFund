name = input("Digite o nome do jogo\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo\n"))
classification = float(input("Informe a nota de classificação do jogo\n"))

if classification > 8.0:
    print(f"O jogo {name} é bom recomendo jogá-lo")
else:
    print(f"O jogo {name} não atingiu uma boa nota. Por isso não recomendo")
