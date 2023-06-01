import random

todasPalavras = ["triangulo", "quadrado", "circulo"]
vidas = 6
letrasUsadas = []
advinhação = []
jogando = True
palavra = random.choice(todasPalavras)

while len(advinhação) < len(palavra):
    advinhação.append("_")

print(palavra)

while vidas > 0 and jogando == True:
    print("".join(advinhação))
    letraAtual = input("Letra: ")
    
    if letraAtual in letrasUsadas:
        print("Já usou essa letra.")
    
    else:
        letrasUsadas.append(letraAtual)
        onde = 0
    
        if palavra.find(letraAtual) == -1:
            vidas -= 1
            print("Letra errada.")
            print(f"Você tem {vidas} vidas restantes.")
    
        while palavra.find(letraAtual, onde) != -1:
            print("Letra certa.")
            advinhação[palavra.find(letraAtual, onde)] = letraAtual
            onde = palavra.find(letraAtual, onde) + 1
    
    if "".join(advinhação) == palavra:
        jogando = False

if vidas == 0:
    print(f'Perdeu, a palavra era: "{palavra}".')
else:
    print(f'A palavra era: "{palavra}".')
    print(f"Ganhou com {vidas} vidas.")