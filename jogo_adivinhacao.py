import random
import os

novo_jogo = 'n'

while novo_jogo == 'n':
    print(f'Seja bem-vindo ao jogo de adivinhação!')
    print(f'Você terá três chances para adivinhar um número entre 1 e 15')

    # Gerar um número aleatório
    num = random.randint(1,15)

    #Jogar
    for i in range(3):
        print(f'\nQual a sua escolha?')
        chute = int(input())

        if chute == num:
            print(f'\nParabéns, você acertou!!!')
            break
        elif chute > num:
            print(f'O número informado é maior que o número a ser adivinhado ')
        else: 
            print(f'O número informado é menor que o número a ser adivinhado ')
    #Caso o jogador não tenha acertado, dizer qual o número secreto:

    if chute != num:
        print(f'\nO número secreto era o {num}')

    novo_jogo = input('Deseja jogar de novo? Digite N para iniciar um novo jogo ou digite outra tecla para finalizar ')
    novo_jogo = novo_jogo.lower()

    #Limpar a tela

    os.system('clear')
    