print("Olá! Vamos jogar Pedra, Papel ou Tesoura!")
jogador1 = input("Insira o nome do primeiro jogador: ")
jogador2 = input("Insira o nome do segundo jogador: ")

jogada1 = input(f"{jogador1}, faça a sua escolha: pedra, papel ou tesoura? ")
jogada2 = input(f"{jogador2}, faça a sua escolha: pedra, papel ou tesoura? ")

if jogada1 == "pedra" and jogada2 == "pedra":
    print("Empate! Jogue novamente.")
elif jogada1 == "pedra" and jogada2 == "tesoura":
    print(f"{jogador1} venceu! Pedra quebra a tesoura.")
elif jogada1 == "pedra" and "jogada2" == "papel":
    print(f"{jogador2} venceu! Papel cobre a pedra.")
elif jogada1 == "papel" and jogada2 == "pedra":
    print(f"{jogador1} venceu! Papel cobre a pedra.")
elif jogada1 == "papel" and jogada2 == "papel":
    print("Empate! Jogue novamente.")
elif jogada1 == "papel" and jogada2 == "tesoura":
    print(f"{jogador2} venceu! Tesoura corta o papel.")
elif jogada1 == "tesoura" and jogada2 == "pedra":
    print(f"{jogador2} venceu! Pedra quebra a tesoura.")
elif jogada1 == "tesoura" and jogada2 == "papel":
    print(f"{jogador1} venceu! Tesoura corta o papel.")
else:
    print("Empate! Jogue novamente!")