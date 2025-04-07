import random
import os

novo_jogo_facil = 'f'
novo_jogo_medio = 'm'
novo_jogo_dificil = 'd'

#Por padrão o jogo começa no fácil, após o primeiro jogo o jogador decide se quer continuar na mesma dificuldade, ou aumentar o nível do desafio.

modo = 'f'

while True:
    os.system('clear')
    print('Seja bem-vindo ao jogo de adivinhação')

    #Define o range dos números de acordo com a dificuldade:

    if modo == 'f':
        print('Você terá três chances de adivinhar um número entre 1 e 15')
        numero_secreto = random.randint(1, 15)
    elif modo == 'm':
        print('Você terá três chances de adivinhar um número entre 1 e 25')
        numero_secreto = random.randint(1, 25)
    elif modo == 'd':
        print('Você terá três chances de adivinhar um número entre 1 e 50')
        numero_secreto = random.randint(1, 50)
    else:
        print('Modo inválido. Encerrando o jogo.')
        break

    acertou = False

    #Verifica se o que o jogador informou é um número válido:

    for i in range(3):
        try:
            chute = int(input('\nQual a sua escolha? '))
        except ValueError:
            print("Entrada inválida! Digite um número.")
            continue

    #Realiza as verificações dos números que o jogador vai informando e define o output de acordo com a escolha dele:

        if chute == numero_secreto:
            print('Parabéns, você acertou!!!')
            acertou = True
            break
        elif chute > numero_secreto:
            print('O número informado é maior que o número a ser adivinhado')
        else:
            print('O número informado é menor que o número a ser adivinhado')

    #Se o jogador não acertou nas 3 tentativas, revela o número secreto

    if not acertou:
        print(f'\nO número secreto era {numero_secreto}')

    #Após o primeiro jogo, o player pode escolher continuar no nível fácil, ou mudar para os níveis médio ou difícil:

    modo = input(f'\n Deseja jogar de novo?\nDigite:\nF - Fácil\nM - Médio\nD - Difícil\nOutra tecla para sair: '.lower()) #Converte a letra para minuscula nos casos onde o player digitou em caixa alta

    #Caso o player digite algo diferente do esperado, encerra o jogo

    if modo not in ['f', 'm', 'd']:
        print('Até a próxima! Obrigado por jogar!')
        break
