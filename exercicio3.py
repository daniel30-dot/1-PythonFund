# Desafio 1
distance = float(input("Digite a distância em Km/h a ser percorrida\n"))

if distance <=200:
    ticket = distance * 0.5
else:
    ticket = distance * 0.35
print(f"O valor da sua passagem é: R$ {ticket:.2f}")

# Desafio 2
salary = float(input("Qual sua faixa salarial atualmente?\n"))
perc_increase = 0.15

if salary >1250:
    perc_increase = 0.10
increase = salary * perc_increase
print(f"Aumento salarial: R$ {increase}")