# Desafio 1

name = input("Digite o nome do jogo\n")
char = name[0].lower()
new_name = name.replace(char, '$')
new_name = char + new_name[1:0]
print(new_name)

# Desafio 2

st1 = 'cab' #zyx
st2 = 'zyx' #cab

new_st1 = st2[:2] + st1[2:]
new_st2 = st1[:2] + st2[2:]

print(new_st1)
print(new_st2)