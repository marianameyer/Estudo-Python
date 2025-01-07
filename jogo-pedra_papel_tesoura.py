# Criação do jogo Pedra, Papel e Tesoura

import random

print('Bem vindo ao jogo: Pedra, Papel e Tesoura! \nVamos começar?')
i = int(input('Quantas vezes você quer jogar? '))

print('\n')

i0 = 0

# Loop para o jogo rodar quantas vezes o usuário deseja:

while i0<i:

# Entrada do usuário. Para evitar erros, irei substituir todas as letras para minúsculas:

    ent_usuario = str(input('Qual sua opção? '))
    ent_usuario = ent_usuario.lower()

# Geração aleatória da escolha do computador:

    escolha_pc = random.choice(['pedra','papel','tesoura'])

    print('Você escolheu',ent_usuario,'e o computador escolheu',escolha_pc)

# Análise do jogo:

    if ent_usuario=='pedra':
        if escolha_pc=='pedra':
            print('Empate!')
        elif escolha_pc=='papel':
            print('Você perdeu!')
        else:
            print('Parabéns! Você venceu!')

    elif ent_usuario=='papel':
        if escolha_pc=='pedra':
            print('Parabéns! Você venceu!')
        elif escolha_pc=='papel':
            print('Empate!')
        else:
            print('Você perdeu!')

    elif ent_usuario=='tesoura':
        if escolha_pc=='pedra':
            print('Você perdeu!')
        elif escolha_pc=='papel':
            print('Parabéns! Você venceu!')
        else:
            print('Empate!')

    else:
        print('Essa opção não existe! Você perdeu a jogada...')

    print('\n')
    i0+=1

print('Tchau!')

