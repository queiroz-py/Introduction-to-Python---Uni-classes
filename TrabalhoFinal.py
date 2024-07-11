import random

def Sudoku():
    escolha = input("Deseja adicionar um sudoku de fora ou gerar um novo? (Adicionar/Gerar): ").lower()
    if escolha == "adicionar":
        #Separa e atribui à lista sudoku cada número digitado no input abaixo
        sudoku = [int(num) for num in input("Digite o sudoku; separando os números por um espaço e substituindo as casas vazias por 0: ").split()]
        #Converte a lista linear em uma lista de listas (matriz 9x9) para representar o tabuleiro de Sudoku, dividindo a lista a cada 9 elementos
        sudoku = [sudoku[i:i+9] for i in range(0, len(sudoku), 9)]
        print("Tabuleiro Adicionado foi:")
        imprimir(sudoku)

    elif escolha == "gerar":
        sudoku = [[0] * 9 for _ in range(9)] #Cria o tabuleiro só de 0 (matriz 9x9)
        print("Dificuldades: Fácil(F), Médio(M), Difícil(D)")
        dificuldade = input("Escolha a dificuldade do jogo a ser gerado pelo programa (F, M ou D): ").lower()
        if dificuldade in ['f', 'm', 'd']: #Verifica se a dificuldade escolhida é válida
            if gerador(sudoku, dificuldade): #Verifica se o sudoku foi gerado com sucesso
                print("Tabuleiro gerado:")
                imprimir(sudoku)
            #Evitando erros de input do usuário, ou erros de geração do sudoku pelo código
            else:
                print("\nNão foi possível gerar um tabuleiro válido.")
                Sudoku()
        else:
            print("Escolha de dificuldade inválida.")
            Sudoku()
    else:
        print("Escolha inválida.")
        Sudoku()
    if solucionar(sudoku): #Verifica se o sudoku possui uma solução
        print("\nSolução encontrada:")
        imprimir(sudoku)
    else:
        print("\nNão foi possível encontrar uma solução.")
        Sudoku()

#Função que printa o tabuleiro
def imprimir(sudoku):
    for i, linha in enumerate(sudoku):
        #formatação das linhas
        if i % 3 == 0 and i != 0:
            print("------+-------+------")
        #formatação das colunas
        for j, num in enumerate(linha):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(num if num != 0 else ".", end=" ")
        print()

#Função que verifica a opção está seguindo as regras do jogo
def regras(sudoku, linha, coluna, num):
    for i in range(9): #Verifica se o número já existe na linha ou coluna
        if sudoku[linha][i] == num or sudoku[i][coluna] == num:
            return False
    #Acha em qual subquadrado cada célula (x,y) está, verificando se não há nenhum número (célula) repetido no subquadrado
    inicioLi, inicioCo = 3 * (linha // 3), 3 * (coluna // 3)
    for i in range(3):
        for j in range(3):
            if sudoku[inicioLi + i][inicioCo + j] == num:
                return False
    return True

#Função que gera o jogo
def gerador(sudoku, dificuldade):
    #Função que preenche a tabela
    def preencher(sudoku):
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0:
                    for num in range(1, 10):
                        if regras(sudoku, i, j, num):
                            sudoku[i][j] = num
                            if preencher(sudoku):
                                return True
                            sudoku[i][j] = 0
                    return False
        return True

    if preencher(sudoku):
        #Depois que a tabela é preenchida, remove os números conforme a dificuldade.
        removidos = {'f': 30, 'm': 40, 'd': 55}.get(dificuldade, 0) #se for outra dificuldade retorna 0
        while removidos > 0:
            i, j = random.randint(0, 8), random.randint(0, 8)
            if sudoku[i][j] != 0:
                sudoku[i][j] = 0
                removidos -= 1
        return True
    return False

#Função que soluciona o tabuleiro
def solucionar(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0: #Verifica se a célula é vazia
                for num in range(1, 10):
                    if regras(sudoku, i, j, num): #Verifica se o número obedece as regras do jogo
                        sudoku[i][j] = num
                        if solucionar(sudoku): #Chama a função novamente para verificar se com esse número encontra uma solução
                            return True #Retorna True caso encontre uma solução
                        sudoku[i][j] = 0
                return False #Retorna False caso não seja possivel solucionar o jogo
    return True #Retorna True caso encontre uma solução

'''
Agora vamos testar o código:

Sudokus testes para adicionar:

Válidos:

0 0 0 0 0 0 8 3 0 0 3 5 4 8 2 1 0 0 0 8 0 0 0 0 0 0 0 0 1 3 2 7 6 0 0 4 8 7 2 0 0 5 0 0 0 6 0 4 0 3 0 2 5 0 9 0 0 0 1 4 0 7 0 0 0 8 0 0 7 0 2 9 3 0 0 0 2 9 5 6 1

5 3 0 0 7 0 0 0 0 6 0 0 1 9 5 0 0 0 0 9 8 0 0 0 0 6 0 8 0 0 0 6 0 0 0 3 4 0 0 8 0 3 0 0 1 7 0 0 0 2 0 0 0 6 0 6 0 0 0 0 2 8 0 0 0 0 4 1 9 0 0 5 0 0 0 0 8 0 0 7 9

Inválido:

5 3 0 0 7 0 0 0 0 6 5 0 1 9 5 0 0 0 0 9 8 0 0 0 0 6 0 8 0 0 0 6 0 0 0 3 4 0 0 8 0 3 0 0 1 7 0 0 0 2 0 0 0 6 0 6 0 0 0 0 2 8 0 0 0 0 4 1 9 0 0 5 0 0 0 0 8 0 0 7 9
'''
Sudoku()
