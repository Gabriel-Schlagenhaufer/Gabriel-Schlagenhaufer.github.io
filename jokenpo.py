import random

continuar = 1  #Variáveis que serão usadas posteriormente
jogador1 = "Primeiro Humano"
jogador2 = "Segundo Humano"
placar1 = 0
placar2 = 0
modalidade = 0

print("\nJokenpô Eletrônico\n"
    "Que modalidade você escolhe?\n"
    "1) Humano x Humano\n"
    "2) Humano x Computador\n"
    "3) Computador x Computador")
while modalidade < 1 or modalidade > 3:
    modalidade = int(input("Digite a modalidade (1, 2, 3): "))  #Escolha da modalidade
    if modalidade < 1 or modalidade > 3:
        print("Opção inválida,  escolha novamente.")

while continuar == 1:  #Se for diferente de 1 quer dizer que a pessoa escolheu parar
    
    escolha1 = 0  #Resetar as variáveis para usar mais uma vez
    escolha2 = 0
    continuar = 0

    if modalidade == 1:  #Checagem da modalidade
        print("\nAs opções de jogada são:\n"
            "1) Pedra\n"
            "2) Papel\n"
            "3) Tesoura")
        while escolha1 < 1 or escolha1 > 3:  #Checar para ver se é uma resposta válida
            escolha1 = int(input("O que o primeiro jogador quer jogar (1, 2, 3): "))  #Escolha das jogadas
            if escolha1 < 1 or escolha1 > 3:
                print("Opção inválida,  escolha novamente.")
        while escolha2 < 1 or escolha2 > 3:
            escolha2 = int(input("O que o segundo jogador quer jogar (1, 2, 3): "))
            if escolha2 < 1 or escolha2 > 3:
                print("Opção inválida,  escolha novamente.")
    elif modalidade == 2:
        jogador1 = "Humano"  #Mudança da variável para utilização posterior
        jogador2 = "Computador"
        print("\nAs opções de jogada são:\n"
            "1) Pedra\n"
            "2) Papel\n"
            "3) Tesoura")
        while escolha1 < 1 or escolha1 > 3:
            escolha1 = int(input("O que o primeiro jogador quer jogar (1, 2, 3): "))  #Escolha das jogadas
            if escolha1 < 1 or escolha1 > 3:
                print("Opção inválida,  escolha novamente.")
        escolha2 = random.randint(1, 3)  #O computador escolhe um número aleatório
        print(f"O computador escolheu: {escolha2}")
    else:
        jogador1 = "Primeiro Computador"
        jogador2 = "Segundo Computador"
        print("\nAs opções de jogada são:\n"
            "1) Pedra\n"
            "2) Papel\n"
            "3) Tesoura")
        escolha1 = random.randint(1, 3)
        escolha2 = random.randint(1, 3)
        print(f"O computador 1 escolheu: {escolha1}\n"
            f"O computador 2 escolheu: {escolha2}")

    if escolha1 == escolha2:  #Checagem do vençedor, o primeiro if é para checagem de empate, o elif é para todos os casos que o jogador 1 ganha e o else é para os casos que o jogador 2 ganha
        print("\nEmpate")
    elif (escolha1 == 1 and escolha2 == 3) or (escolha1 == 2 and escolha2 == 1) or (escolha1 == 3 and escolha2 == 2):
        placar1 += 1  #A variável subirá 1 sempre que o jogador um ganhar
        print(f"\n{jogador1} ganhou!")
    else:
        placar2 += 1
        print(f"\n{jogador2} ganhou!")

    print(f"\nO placar atual é\n"
        f"{jogador1} ({placar1}) x ({placar2}) {jogador2}")
    
    print("\nDeseja continuar?\n"
          "1) Sim\n"
          "2) Não")
    while continuar < 1 or continuar > 2:
        continuar = int(input("Opção (1, 2): "))  #Opção de continuar a jogar
        if continuar < 1 or continuar > 2:
            print("Opção inválida, escolha novamente.")

print(f"O placar final ficou:\n"
      f"{jogador1} ({placar1}) x ({placar2}) {jogador2}")

print("Obrigado por jogar!!\n"
      "Projeto realizado por Gabriel Antony Olsson Schlagenhaufer")