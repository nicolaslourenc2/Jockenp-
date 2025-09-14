# Importa a biblioteca random para as jogadas do computador e pergunta se o usuario deseja ver as regras
import random
print('--------JOCKENPÔ-------')
print('Olá! Seja muito bem vindo ao jogo de jockenpô em python!\n')
print('Deseja conhecer as regras do jogo?\nDigite 1 para Sim\nDigite 2 para Não')

opcao = input('Sua opção: ').strip()

# Verificação para que o usuario digite apenas 1 e 2
while opcao != '1' and opcao != '2':
    print('\nOpção inválida!\nDigite 1 para Sim\nDigite 2 para Não')
    opcao = input('Sua opção: ').strip()

if opcao == '1':
    print('\nO jogo possui 3 simbolos, Pedra, Papel e Tesoura.')
    print('Os jogadores deveram escolher um desses 3 simbolos e fazer sua jogada.')
    print('Pedra ganha de Tesoura')
    print('Tesoura ganha de Papel')
    print('Papel ganha de Pedra')

# Mostra as modalidades para o usuario e pergunta qual ele deseja

print('\nNosso jogo possui as seguintes modadalides que NÂO podem ser alteradas após inicio do jogo.')
print('1 - Humano vs Humano')
print('2 - Humano vs Computador')
print('3 - Computador vs Computador')

opcao1 = input('Digite sua opção: ').strip()

# Variaveis de pontuação de ambos os jogadores
pontuacao1 = 0
pontuacao2 = 0

# Verificação para que o usuario digite apenas 1 e 2
while opcao1 != '1' and opcao1 != '2' and opcao1 != '3':
    print('\nOpção inválida!\nDigite sua opção: ')
    opcao1 = input('Sua opção: ').strip()

# inicio da modalidade 1
if opcao1 == '1':
    print('\nMODALIDADE - HUMANO VS HUMANO')
    print('1 - Pedra')
    print('2 - Papel')
    print('3 - Tesoura')
    jogador1 = input('Jogador 1, digite sua opção: ').strip()
    jogador2 = input('Jogador 2, digite sua opção: ').strip()

    # Verificação para que o jogador 1 digite apenas 1 e 2
    while jogador1 != '1' and jogador1 != '2' and jogador1 != '3':
        jogador1 = input('Jogador 1, digite sua opção: ').strip()

    # Verificação para que o jogador 2 digite apenas 1 e 2
    while jogador2 != '1' and jogador2 != '2' and jogador2 != '3':
        jogador2 = input('Jogador 2, digite sua opção: ').strip()

    # todas as possibildiades de jogadas
    if jogador1 == '1' and jogador2 == '1':
        print('Jogador 1 escolheu Pedra e Jogador 2 escolheu Pedra. EMPATE')
        print(f'Placar: {pontuacao1} x {pontuacao2}')
    elif jogador1 == '2' and jogador2 == '2':
        print('Jogador 1 escolheu Papel e Jogador 2 escolheu Papel. EMPATE')
        print(f'Placar: {pontuacao1} x {pontuacao2}')
    elif jogador1 == '3' and jogador2 == '3':
        print('Jogador 1 escolheu Tesoura e Jogador 2 escolheu Tesoura. EMPATE')
        print(f'Placar: {pontuacao1} x {pontuacao2}')

    elif jogador1 == '1' and jogador2 == '3':
        print('Jogador 1 escolheu Pedra e Jogador 2 escolheu Tesoura. Jogador 1 venceu!')
        pontuacao1 += 1
        print(f'Placar: {pontuacao1} x {pontuacao2}')
    elif jogador1 == '2' and jogador2 == '1':
        print('Jogador 1 escolheu Papel e Jogador 2 escolheu Pedra. Jogador 1 venceu!')
        pontuacao1 += 1
        print(f'Placar: {pontuacao1} x {pontuacao2}')
    elif jogador1 == '3' and jogador2 == '2':
        print('Jogador 1 escolheu Tesoura e Jogador 2 escolheu Papel. Jogador 1 venceu!')
        pontuacao1 += 1
        print(f'Placar: {pontuacao1} x {pontuacao2}')

    elif jogador2 == '1' and jogador1 == '3':
        print('Jogador 2 escolheu Pedra e Jogador 1 escolheu Tesoura. Jogador 2 venceu!')
        pontuacao2 += 1
        print(f'Placar: {pontuacao1} x {pontuacao2}')
    elif jogador2 == '2' and jogador1 == '1':
        print('Jogador 2 escolheu Papel e Jogador 1 escolheu Pedra. Jogador 2 venceu!')
        pontuacao2 += 1
        print(f'Placar: {pontuacao1} x {pontuacao2}')
    elif jogador2 == '3' and jogador1 == '2':
        print('Jogador 2 escolheu Tesoura e Jogador 1 escolheu Papel. Jogador 2 venceu!')
        pontuacao2 += 1
        print(f'Placar: {pontuacao1} x {pontuacao2}')

    # pergunta se o usuario deseja continuar jogando
    print('\n1 - Continuar jogando')
    print('2 - Parar de jogar')
    continuar = input('Sua opção: ').strip()

    # verificação para que o usuario digite apenas 1 ou 2
    while continuar != '1' and continuar != '2':
        continuar = input('Opção incorreta, digite 1 ou 2: ').strip()

    # inicio do looping se o usuario digita 1
    while continuar == '1':
        print('\nMODALIDADE - HUMANO VS HUMANO')
        print('1 - Pedra')
        print('2 - Papel')
        print('3 - Tesoura')
        jogador1 = input('Jogador 1, digite sua opção: ').strip()
        jogador2 = input('Jogador 2, digite sua opção: ').strip()

        # Verificação para que o jogador 1 digite apenas 1 e 2
        while jogador1 != '1' and jogador1 != '2' and jogador1 != '3':
            jogador1 = input('Jogador 1, digite sua opção: ').strip()

        # Verificação para que o jogador 2 digite apenas 1 e 2
        while jogador2 != '1' and jogador2 != '2' and jogador2 != '3':
            jogador2 = input('Jogador 2, digite sua opção: ').strip()

        # todas as possibildiades de jogadas
        if jogador1 == '1' and jogador2 == '1':
            print('Jogador 1 escolheu Pedra e Jogador 2 escolheu Pedra. EMPATE')
            print(f'Placar: {pontuacao1} x {pontuacao2}')
        elif jogador1 == '2' and jogador2 == '2':
            print('Jogador 1 escolheu Papel e Jogador 2 escolheu Papel. EMPATE')
            print(f'Placar: {pontuacao1} x {pontuacao2}')
        elif jogador1 == '3' and jogador2 == '3':
            print('Jogador 1 escolheu Tesoura e Jogador 2 escolheu Tesoura. EMPATE')
            print(f'Placar: {pontuacao1} x {pontuacao2}')

        elif jogador1 == '1' and jogador2 == '3':
            print('Jogador 1 escolheu Pedra e Jogador 2 escolheu Tesoura. Jogador 1 venceu!')
            pontuacao1 += 1
            print(f'Placar: {pontuacao1} x {pontuacao2}')
        elif jogador1 == '2' and jogador2 == '1':
            print('Jogador 1 escolheu Papel e Jogador 2 escolheu Pedra. Jogador 1 venceu!')
            pontuacao1 += 1
            print(f'Placar: {pontuacao1} x {pontuacao2}')
        elif jogador1 == '3' and jogador2 == '2':
            print('Jogador 1 escolheu Tesoura e Jogador 2 escolheu Papel. Jogador 1 venceu!')
            pontuacao1 += 1
            print(f'Placar: {pontuacao1} x {pontuacao2}')

        elif jogador2 == '1' and jogador1 == '3':
            print('Jogador 2 escolheu Pedra e Jogador 1 escolheu Tesoura. Jogador 2 venceu!')
            pontuacao2 += 1
            print(f'Placar: {pontuacao1} x {pontuacao2}')
        elif jogador2 == '2' and jogador1 == '1':
            print('Jogador 2 escolheu Papel e Jogador 1 escolheu Pedra. Jogador 2 venceu!')
            pontuacao2 += 1
            print(f'Placar: {pontuacao1} x {pontuacao2}')
        elif jogador2 == '3' and jogador1 == '2':
            print('Jogador 2 escolheu Tesoura e Jogador 1 escolheu Papel. Jogador 2 venceu!')
            pontuacao2 += 1
            print(f'Placar: {pontuacao1} x {pontuacao2}')

        # pergunta se o usuario deseja continuar jogando
        print('\n1 - Continuar jogando')
        print('2 - Parar de jogar')
        continuar = input('Sua opção: ').strip()

        # verificação para que o usuario digite apenas 1 ou 2
        while continuar != '1' and continuar != '2':
            continuar = input('Opção incorreta, digite 1 ou 2: ').strip()

    # Placar final com mensagem de despedida
    print(f'\nPlacar final {pontuacao1} x {pontuacao2}')
    print('Obrigado por jogar nosso jogo! Feito por Nicolas Lourenço')

# inicio da modalidade 2
elif opcao1 == '2':
    print('\nMODALIDADE - HUMANO VS COMPUTADOR')
    print('1 - Pedra')
    print('2 - Papel')
    print('3 - Tesoura')
    jogador1 = input('Jogador 1, digite sua opção: ').strip()

    # Verificação para que o jogador digite apenas 1 e 2
    while jogador1 != '1' and jogador1 != '2' and jogador1 != '3':
        jogador1 = input('Jogador 1, digite sua opção: ').strip()

    # funcao randint para escolher um numero aleatorio entre 1 e 3 para o computador
    computador = random.randint(1, 3)

    # todas as possibilidades de jogadas
    if jogador1 == '1' and computador == 1:
        print('Jogador 1 escolheu Pedra e computador escolheu Pedra. EMPATE')
        print(f'Placar: {pontuacao1} x {pontuacao2}')
    elif jogador1 == '2' and computador == 2:
        print('Jogador 1 escolheu Papel e computador escolheu Papel. EMPATE')
        print(f'Placar: {pontuacao1} x {pontuacao2}')
    elif jogador1 == '3' and computador == 3:
        print('Jogador 1 escolheu Tesoura e computador escolheu Tesoura. EMPATE')
        print(f'Placar: {pontuacao1} x {pontuacao2}')

    elif jogador1 == '1' and computador == 3:
        print('Jogador 1 escolheu Pedra e computador escolheu Tesoura. Jogador 1 venceu')
        pontuacao1 += 1
        print(f'Placar: {pontuacao1} x {pontuacao2}')
    elif jogador1 == '2' and computador == 1:
        print('Jogador 1 escolheu Papel e computador escolheu Pedra. Jogador 1 venceu')
        pontuacao1 += 1
        print(f'Placar: {pontuacao1} x {pontuacao2}')
    elif jogador1 == '3' and computador == 2:
        print('Jogador 1 escolheu Tesoura e computador escolheu Papel. Jogador 1 venceu')
        pontuacao1 += 1
        print(f'Placar: {pontuacao1} x {pontuacao2}')

    elif computador == 1 and jogador1 == '3':
        print('Jogador 1 escolheu Tesoura e computador escolheu Pedra. Computador venceu')
        pontuacao2 += 1
        print(f'Placar: {pontuacao1} x {pontuacao2}')
    elif computador == 2 and jogador1 == '1':
        print('Jogador 1 escolheu Pedra e computador escolheu Papel. Computador venceu')
        pontuacao2 += 1
        print(f'Placar: {pontuacao1} x {pontuacao2}')
    elif computador == 3 and jogador1 == '2':
        print('Jogador 1 escolheu Papel e computador escolheu Tesoura. Computador venceu')
        pontuacao2 += 1
        print(f'Placar: {pontuacao1} x {pontuacao2}')

    print('\n1 - Continuar jogando')
    print('2 - Parar de jogar')
    continuar = input('Sua opção: ').strip()

    # Verificação para que o usuario digite apenas 1 ou 2
    while continuar != '1' and continuar != '2':
        continuar = input('Opção incorreta, digite 1 ou 2: ').strip()

    # Inicio do looping se o usuario digita 1
    while continuar == '1':
        print('1 - Pedra')
        print('2 - Papel')
        print('3 - Tesoura')
        jogador1 = input('Jogador 1, digite sua opção: ').strip()

        # Verificação para que o usuario apenas digite 1 ou 2
        while jogador1 != '1' and jogador1 != '2' and jogador1 != '3':
            jogador1 = input('Jogador 1, digite sua opção: ').strip()

        computador = random.randint(1, 3)

        if jogador1 == '1' and computador == 1:
            print('Jogador 1 escolheu Pedra e computador escolheu Pedra. EMPATE')
            print(f'Placar: {pontuacao1} x {pontuacao2}')
        elif jogador1 == '2' and computador == 2:
            print('Jogador 1 escolheu Papel e computador escolheu Papel. EMPATE')
            print(f'Placar: {pontuacao1} x {pontuacao2}')
        elif jogador1 == '3' and computador == 3:
            print('Jogador 1 escolheu Tesoura e computador escolheu Tesoura. EMPATE')
            print(f'Placar: {pontuacao1} x {pontuacao2}')

        elif jogador1 == '1' and computador == 3:
            print('Jogador 1 escolheu Pedra e computador escolheu Tesoura. Jogador 1 venceu')
            pontuacao1 += 1
            print(f'Placar: {pontuacao1} x {pontuacao2}')
        elif jogador1 == '2' and computador == 1:
            print('Jogador 1 escolheu Papel e computador escolheu Pedra. Jogador 1 venceu')
            pontuacao1 += 1
            print(f'Placar: {pontuacao1} x {pontuacao2}')
        elif jogador1 == '3' and computador == 2:
            print('Jogador 1 escolheu Tesoura e computador escolheu Papel. Jogador 1 venceu')
            pontuacao1 += 1
            print(f'Placar: {pontuacao1} x {pontuacao2}')

        elif computador == 1 and jogador1 == '3':
            print('Jogador 1 escolheu Tesoura e computador escolheu Pedra. Computador venceu')
            pontuacao2 += 1
            print(f'Placar: {pontuacao1} x {pontuacao2}')
        elif computador == 2 and jogador1 == '1':
            print('Jogador 1 escolheu Pedra e computador escolheu Papel. Computador venceu')
            pontuacao2 += 1
            print(f'Placar: {pontuacao1} x {pontuacao2}')
        elif computador == 3 and jogador1 == '2':
            print('Jogador 1 escolheu Papel e computador escolheu Tesoura. Computador venceu')
            pontuacao2 += 1
            print(f'Placar: {pontuacao1} x {pontuacao2}')

        print('\n1 - Continuar jogando')
        print('2 - Parar de jogar')
        continuar = input('Sua opção: ').strip()

        while continuar != '1' and continuar != '2':
            continuar = input('Opção incorreta, digite 1 ou 2: ').strip()

    # Placar final e mensagem de despedida
    print(f'\nPlacar final {pontuacao1} x {pontuacao2}')
    print('Obrigado por jogar nosso jogo! Feito por Nicolas Lourenço')

# Inicio da modalidade 3
elif opcao1 == '3':
    print('\nMODALIDADE - COMPUTADOR VS COMPUTADOR')
    print('1 - Pedra')
    print('2 - Papel')
    print('3 - Tesoura')

    # Função randint para sortear um numero aleatorio entre 1 e 3 para ambas as variaveis dos computadores
    computador = random.randint(1, 3)
    computador2 = random.randint(1, 3)

    # Todas as possibilidades de jogada
    if computador == 1 and computador2 == 1:
        print('Computador 1 escolheu Pedra e Computador 2 escolheu Pedra. EMPATE')
        print(f'Placar: {pontuacao1} x {pontuacao2}')
    elif computador == 2 and computador2 == 2:
        print('Computador 1 escolheu Papel e Computador 2 escolheu Papel. EMPATE')
        print(f'Placar: {pontuacao1} x {pontuacao2}')
    elif computador == 3 and computador2 == 3:
        print('Computador 1 escolheu Tesoura e computador 2 escolheu Tesoura. EMPATE')
        print(f'Placar: {pontuacao1} x {pontuacao2}')

    elif computador == 1 and computador2 == 3:
        print('Computador 1 escolheu Pedra e Computador 2 escolheu Tesoura. Computador 1 venceu')
        pontuacao1 += 1
        print(f'Placar: {pontuacao1} x {pontuacao2}')
    elif computador == 2 and computador2 == 1:
        print('Computador 1 escolheu Papel e Computador escolheu Pedra. Computador 1 venceu')
        pontuacao1 += 1
        print(f'Placar: {pontuacao1} x {pontuacao2}')
    elif computador == 3 and computador2 == 2:
        print('Computador 1 escolheu Tesoura e Computador 2 escolheu Papel. Computador 1 venceu')
        pontuacao1 += 1
        print(f'Placar: {pontuacao1} x {pontuacao2}')

    elif computador2 == 1 and computador == 3:
        print('Computador 1 escolheu Tesoura e Computador 2 escolheu Pedra. Computador 2 venceu')
        pontuacao2 += 1
        print(f'Placar: {pontuacao1} x {pontuacao2}')
    elif computador2 == 2 and computador == 1:
        print('Computador 1 escolheu Pedra e Computador 2 escolheu Papel. Computador 2 venceu')
        pontuacao2 += 1
        print(f'Placar: {pontuacao1} x {pontuacao2}')
    elif computador2 == 3 and computador == 2:
        print('Computador 1 escolheu Papel e Computador 2 escolheu Tesoura. Computador 2 venceu')
        pontuacao2 += 1
        print(f'Placar: {pontuacao1} x {pontuacao2}')

    print('\n1 - Continuar jogando')
    print('2 - Parar de jogar')
    continuar = input('Sua opção: ').strip()

    # Verificação se o usuario digita apenas 1 ou 2
    while continuar != '1' and continuar != '2':
        continuar = input('Opção incorreta, digite 1 ou 2: ').strip()

    # Inicio do looping
    while continuar == '1':
        print('\nMODALIDADE - COMPUTADOR VS COMPUTADOR')
        print('1 - Pedra')
        print('2 - Papel')
        print('3 - Tesoura')

        computador = random.randint(1, 3)
        computador2 = random.randint(1, 3)

        if computador == 1 and computador2 == 1:
            print('Computador 1 escolheu Pedra e Computador 2 escolheu Pedra. EMPATE')
            print(f'Placar: {pontuacao1} x {pontuacao2}')
        elif computador == 2 and computador2 == 2:
            print('Computador 1 escolheu Papel e Computador 2 escolheu Papel. EMPATE')
            print(f'Placar: {pontuacao1} x {pontuacao2}')
        elif computador == 3 and computador2 == 3:
            print('Computador 1 escolheu Tesoura e computador 2 escolheu Tesoura. EMPATE')
            print(f'Placar: {pontuacao1} x {pontuacao2}')

        elif computador == 1 and computador2 == 3:
            print('Computador 1 escolheu Pedra e Computador 2 escolheu Tesoura. Computador 1 venceu')
            pontuacao1 += 1
            print(f'Placar: {pontuacao1} x {pontuacao2}')
        elif computador == 2 and computador2 == 1:
            print('Computador 1 escolheu Papel e Computador escolheu Pedra. Computador 1 venceu')
            pontuacao1 += 1
            print(f'Placar: {pontuacao1} x {pontuacao2}')
        elif computador == 3 and computador2 == 2:
            print('Computador 1 escolheu Tesoura e Computador 2 escolheu Papel. Computador 1 venceu')
            pontuacao1 += 1
            print(f'Placar: {pontuacao1} x {pontuacao2}')

        elif computador2 == 1 and computador == 3:
            print('Computador 1 escolheu Tesoura e Computador 2 escolheu Pedra. Computador 2 venceu')
            pontuacao2 += 1
            print(f'Placar: {pontuacao1} x {pontuacao2}')
        elif computador2 == 2 and computador == 1:
            print('Computador 1 escolheu Pedra e Computador 2 escolheu Papel. Computador 2 venceu')
            pontuacao2 += 1
            print(f'Placar: {pontuacao1} x {pontuacao2}')
        elif computador2 == 3 and computador == 2:
            print('Computador 1 escolheu Papel e Computador 2 escolheu Tesoura. Computador 2 venceu')
            pontuacao2 += 1
            print(f'Placar: {pontuacao1} x {pontuacao2}')

        print('\n1 - Continuar jogando')
        print('2 - Parar de jogar')
        continuar = input('Sua opção: ').strip()

        while continuar != '1' and continuar != '2':
            continuar = input('Opção incorreta, digite 1 ou 2: ').strip()

    # Placar final e mensagem de despedida
    print(f'\nPlacar final {pontuacao1} x {pontuacao2}')
    print('Obrigado por jogar nosso jogo! Feito por Nicolas Lourenço')
