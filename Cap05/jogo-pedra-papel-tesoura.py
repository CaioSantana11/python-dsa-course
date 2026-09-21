print("Olá! Vamos jogar Pedra, Papel ou Tesoura!")
print("Regras: escolha entre 'pedra'. 'papel' ou 'tesoura'.")

#Importante lembrar de fazer a limpeza de dados, não sabemos como o humano irá inserir os dados (letras maiúsculas, com espaços, etc)

jogador1 = input("Insira o nome do primeiro jogador: ")
jogador2 = input("Insira o nome do segundo jogador: ")

jogada1 = input(f"{jogador1}, faça a sua escolha: pedra, papel ou tesoura? ").strip().lower().replace(" ", "")
jogada2 = input(f"{jogador2}, faça a sua escolha: pedra, papel ou tesoura? ").strip().lower().replace(" ", "")

if jogada1 == jogada2:
    print("Empate! Jogue novamente.")
elif jogada1 == "tesoura" and jogada2 == "papel" or \
    jogada1 == "pedra" and jogada2 == "tesoura" or \
    jogada1 == "papel" and jogada2 == "pedra":
    print(f"{jogador1} venceu!")
else:
    print(f"{jogador2} venceu!")
