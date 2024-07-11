import random

#Definindo as funções que vão ter papéis dentro do jogo (def main)

def matriz(tamanho):
    pares = list(range(1, (tamanho * tamanho // 2) + 1)) * 2
    random.shuffle(pares)

    #Criando uma matriz como * e outra com os números para serem comparadas
    Moculta = [['*' for _ in range(tamanho)] for _ in range(tamanho)]
    Mnúmeros = [[0 for _ in range(tamanho)] for _ in range(tamanho)]

    #Assinalando os números aleatórios
    index = 0
    for i in range(tamanho):
        for j in range (tamanho):
            Mnúmeros[i][j] = pares [index]
            index += 1
    
    return Moculta, Mnúmeros

#Formatação da Matriz * 
def Print(Moculta):
    tamanho = len(Moculta)
    #Cabeçalho para as colunas
    print("   " + " ".join(map(str, range(tamanho))))
    #Cabeçalho para as linhas
    for k, linhas in enumerate(Moculta):
        print(f"{k}  {' '.join(map(str, linhas))}")
    print()

#Definindo as jogadas dos jogadores
def Entrada(tamanho):
    while True:
        try:
            entrada = input("Escolha uma posição y,x (ex: 0,0): ")
            x, y = map(int, entrada.split(","))
            if 0 <= x < tamanho and 0 <= y < tamanho:
                return x, y
            else:
                print(f"Coordenadas fora dos limites. Tente novamente com valores entre 0 e {tamanho-1}.")
        except ValueError:
            print("Entrada inválida. Digite dois números separados por vírgula.")

#Esqueleto do jogo
def Jogo():
    print("Bem-vindo ao Jogo da Memória!")

    #Tamanho do Jogo
    while True:
        try: 
            tamanho = int(input("Escolha o tamanho do seu jogo (2,4,6,8,10): "))
            if 2 <= tamanho <= 10 and (tamanho*tamanho) % 2 == 0:
                break
            else:
                print("O tamanho da matriz deve ser entre 2 e 10 e deve ter um número par de casas.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro entre 2 e 10.")
    
    Moculta, Mnúmeros = matriz(tamanho)

    #Número de Jogadores
    while True:
        try:
            jogadores = int(input("Número de Jogadores (1-4): "))
            if 1 <= jogadores <= 4:
                break
            else:
                print("Tente Novamente")
        except ValueError:
            print("Entrada Inválida. Digite um número entre 1 e 4.")
    
    #Pontuação
    pontuação = [0]*jogadores
    jogador = 0
    acertos = 0

    while acertos < ((tamanho * tamanho) // 2):
        Print(Moculta)
        print(f"É a vez do Jogador {jogador + 1}!")

        acertou = True
        while acertou and acertos < ((tamanho * tamanho // 2)):
            #Primeiro chute
            x1, y1 = Entrada(tamanho)

            if Moculta[x1][y1] != "*":
                print("Você já escolheu esta posição. Tente novamente.")
                continue

            Moculta[x1][y1] = Mnúmeros[x1][y1]
            Print(Moculta)

            #Segundo Chute:4
            x2, y2 = Entrada(tamanho)

            if Moculta[x2][y2] != '*':
                print("Você já escolheu esta posição. Tente novamente.")
                Moculta[x1][y1] = '*'
                continue

            Moculta[x2][y2] = Mnúmeros[x2][y2]
            Print(Moculta)

            if Mnúmeros[x1][y1] == Mnúmeros[x2][y2]:
                print("Parabéns! Você encontrou um par!")
                acertos += 1
                pontuação[jogador] += 1
                print(f"Jogador {jogador + 1} encontrou um par e tem agora {pontuação[jogador]} pontos.")
            else:
                print("Você errou. Próximo jogador.")
                Moculta[x1][y1] = '*'
                Moculta[x2][y2] = '*'
                acertou = False

        if not acertou:
            jogador = (jogador + 1) % jogadores
    
    print(f"Parabéns! Você completou o jogo!")
    print("Pontuações finais:")

    for w in range(jogadores):
        print(f"Jogador {w + 1}: {pontuação[w]} pontos")
    
Jogo()

