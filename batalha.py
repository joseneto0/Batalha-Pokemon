from time import sleep
from random import randint
import funções


while True:
    charizard_ataques = {"Air Slash": 10, "Heat Wave": 14, "Dragon Claw": 10, "Flare Blitz": 8}
    limites_char = [8, 3, 4, 10]
    vida_charizard = 70

    rayquaza_ataques = {"Hyper Beam": 12, "Ice Beam": 10, "Outrage": 15, "Seismic Toss": 10}
    vida_rayquaza = 70
    limites_ray = [3, 4, 2, 4]
    jogada_rayquaza = randint(0, 3)

    blastoise_ataques = {"Hydro Pump": 15, "Water Gun": 8, "Hydro Cannon": 11, "Ice Beam": 12}
    limites_blas = [2, 10, 4, 3]
    vida_blastoise = 70

    venusaur_ataques = {"Vine Whip": 13, "Solar Beam": 16, "Razor Leaf": 10, "Tackle": 8}
    limites_ven = [1, 1, 5, 5]
    vida_venusaur = 70

    funções.linha()
    print(f'{"BATALHA POKEMON":^40}')
    funções.linha()
    print("""Escolha seu pokemon:
    [1] - Charizard
    [2] - Blastoise 
    [3] - Venusaur
    """)
    escolha = int(input('Digite sua escolha: '))
    while escolha < 1 or escolha > 3:
        escolha = int(input('Pô mano, escolha certo :). Digite sua escolha: '))

    #charizard
    if escolha == 1:
        funções.linha()
        print('\033[1;31mParabéns! Você escolheu o Charizard\033[m')
        sleep(1)
        print(f'O seu pokemon tem {vida_charizard} de vida')
        sleep(1)
        print('Os ataques deles são: ')
        for i, e in enumerate(charizard_ataques):
            print(f'{i} - {e}: {charizard_ataques[e]} de ataque, com limite de {limites_char[i]} vezes')
            sleep(1)
        funções.linha()
        print("OH NÃO!")
        sleep(1)
        print("\033[1;32mUM RAYQUAZA APARECEU!\033[m")
        sleep(1)
        print("\033[1;31mLUTE PELA SUA VIDA, MESTRE POKEMON\033[m")
        sleep(1)
        print(f'O pokemon RAYQUAZA tem {vida_rayquaza} de vida')

        #Pegar os valores do dicionario (ataque e dano do ataque)
        #charizard
        values_char = list(charizard_ataques.values())
        keys_char = list(charizard_ataques.keys())
        #rayquaza
        values_ray = list(rayquaza_ataques.values())
        keys_ray = list(rayquaza_ataques.keys())

        #batalha começa
        while True:

            #jogada do jogador
            funções.linha()
            sleep(0.7)
            print('\033[1;31mVEZ DO CHARIZARD\033[m')
            ataque = int(input('Qual vai ser seu ataque? [4 - rever os ataques] '))
            ataque = funções.ataque_4(ataque, charizard_ataques)
            while ataque < 0 or ataque > 4:
                ataque = int(input('\033[1;31mNÚMERO INVÁLIDO.\033[m Qual vai ser seu ataque? [4 - rever os ataques] '))
            if ataque == 0 or ataque == 1 or ataque == 2 or ataque == 3:
                while limites_char[ataque] == 0:
                    ataque = int(input('\033[1;31mLIMITE ZERADO\033[m. Escolha outro ataque: [4 - rever os ataques] '))
                    ataque = funções.ataque_4(ataque, charizard_ataques)
            sleep(0.7)
            print(f'Você ativou o ataque {keys_char[ataque]}, que da {values_char[ataque]} de dano, você pode utiliza-lo {limites_char[ataque]-1} vezes')
            limites_char[ataque] -= 1
            sleep(0.7)
            print(f'O Rayquaza agora está com \033[1;31m{funções.vida(vida_rayquaza, values_char[ataque])}\033[m de vida')
            vida_rayquaza = funções.vida(vida_rayquaza, values_char[ataque])
            if vida_rayquaza == 0:
                funções.linha()
                print(f'\033[1;92mPARABÉNS! VOCÊ VENCEU\033[m')
                break
            funções.linha()
            sleep(0.7)

            #jogadas do pc
            print(f'\033[1;92mVEZ DO RAYQUAZA\033[m')
            sleep(0.7)
            print(f'Rayquaza ativou o ataque {keys_ray[jogada_rayquaza]}, que da {values_ray[jogada_rayquaza]} de dano, com limite de {limites_ray[jogada_rayquaza]-1}')
            limites_ray[jogada_rayquaza] -= 1
            while limites_ray[jogada_rayquaza] == 0:
                jogada_rayquaza = randint(0, 3)
            sleep(0.7)
            print(f'Agora o Charizard está com \033[1;31m{funções.vida(vida_charizard, values_ray[jogada_rayquaza])}\033[m de vida')
            vida_charizard = funções.vida(vida_charizard, values_ray[jogada_rayquaza])
            if vida_charizard == 0:
                funções.linha()
                print(f'\033=1;31mVOCÊ PERDEU! :C\033[m')
                break
            sleep(0.7)

    #Blastoise
    if escolha == 2:
        funções.linha()
        print('\033[1;34mParabéns! Você escolheu o Blastoise\033[m')
        sleep(1)
        print(f'O seu pokemon tem {vida_blastoise} de vida')
        sleep(1)
        print('Os ataques deles são: ')
        for i, e in enumerate(blastoise_ataques):
            print(f'{i} - {e}: {blastoise_ataques[e]} de ataque, com limite de {limites_blas[i]} vezes')
            sleep(1)
        funções.linha()
        print("OH NÃO!")
        sleep(1)
        print("\033[1;31mUM RAYQUAZA APARECEU!\033[m")
        sleep(1)
        print("\033[1;31mLUTE PELA SUA VIDA, MESTRE POKEMON\033[m")
        sleep(1)
        print(f'O pokemon RAYQUAZA tem {vida_rayquaza} de vida')

        # Pegar os valores do dicionario (ataque e dano do ataque)
        # blastoise
        values_blas = list(blastoise_ataques.values())
        keys_blas = list(blastoise_ataques.keys())
        # rayquaza
        values_ray = list(rayquaza_ataques.values())
        keys_ray = list(rayquaza_ataques.keys())

        #batalha começa
        while True:

            # jogada do jogador
            funções.linha()
            sleep(0.7)
            print('\033[1;34mVEZ DO BLASTOISE\033[m')
            ataque = int(input('Qual vai ser seu ataque? [4 - rever os ataques] '))
            ataque = funções.ataque_4(ataque, blastoise_ataques)
            while ataque < 0 or ataque > 4:
                ataque = int(input('\033[1;31mNÚMERO INVÁLIDO.\033[m Qual vai ser seu ataque? [4 - rever os ataques] '))
            if ataque == 0 or ataque == 1 or ataque == 2 or ataque == 3:
                while limites_blas[ataque] == 0:
                    ataque = int(input('\033[1;31mLIMITE ZERADO\033[m. Escolha outro ataque: [4 - rever os ataques] '))
                    ataque = funções.ataque_4(ataque, blastoise_ataques)
            sleep(0.7)
            print(f'Você ativou o ataque {keys_blas[ataque]}, que da {values_blas[ataque]} de dano, você pode utiliza-lo {limites_blas[ataque] - 1} vezes')
            limites_blas[ataque] -= 1
            sleep(0.7)
            print(f'O Rayquaza agora está com \033[1;31m{funções.vida(vida_rayquaza, values_blas[ataque])}\033[m de vida')
            vida_rayquaza = funções.vida(vida_rayquaza, values_blas[ataque])
            if vida_rayquaza == 0:
                funções.linha()
                print(f'\033[1;92mPARABÉNS! VOCÊ VENCEU\033[m')
                break
            funções.linha()
            sleep(0.7)

            # jogadas do pc
            print(f'\033[1;92mVEZ DO RAYQUAZA\033[m')
            sleep(0.7)
            print(f'Rayquaza ativou o ataque {keys_ray[jogada_rayquaza]}, que da {values_ray[jogada_rayquaza]} de dano, com limite de {limites_ray[jogada_rayquaza] - 1}')
            limites_ray[jogada_rayquaza] -= 1
            while limites_ray[jogada_rayquaza] == 0:
                jogada_rayquaza = randint(0, 3)
            sleep(0.7)
            print(f'Agora o Blastoise está com \033[1;31m{funções.vida(vida_blastoise, values_ray[jogada_rayquaza])}\033[m de vida')
            vida_blastoise = funções.vida(vida_blastoise, values_ray[jogada_rayquaza])
            if vida_blastoise == 0:
                funções.linha()
                print(f'\033=1;31mVOCÊ PERDEU! :C\033[m')
                break
            sleep(0.7)

    #venusaur
    if escolha == 3:
        funções.linha()
        print('\033[1;92mParabéns! Você escolheu o Venusaur\033[m')
        sleep(1)
        print(f'O seu pokemon tem {vida_venusaur} de vida')
        sleep(1)
        print('Os ataques deles são: ')
        for i, e in enumerate(venusaur_ataques):
            print(f'{i} - {e}: {venusaur_ataques[e]} de ataque, com limite de {limites_ven[i]} vezes')
            sleep(1)
        funções.linha()
        print("OH NÃO!")
        sleep(1)
        print("\033[1;32mUM RAYQUAZA APARECEU!\033[m")
        sleep(1)
        print("\033[1;31mLUTE PELA SUA VIDA, MESTRE POKEMON\033[m")
        sleep(1)
        print(f'O pokemon RAYQUAZA tem {vida_rayquaza} de vida')

        #Pegar os valores do dicionario (ataque e dano do ataque)
        #charizard
        values_ven = list(venusaur_ataques.values())
        keys_ven = list(venusaur_ataques.keys())
        #rayquaza
        values_ray = list(rayquaza_ataques.values())
        keys_ray = list(rayquaza_ataques.keys())

        #batalha começa
        while True:

            #jogada do jogador
            funções.linha()
            sleep(0.7)
            print('\033[1;92mVEZ DO VENUSAUR\033[m')
            ataque = int(input('Qual vai ser seu ataque? [4 - rever os ataques] '))
            ataque = funções.ataque_4(ataque, venusaur_ataques)
            while ataque < 0 or ataque > 4:
                ataque = int(input('\033[1;31mNÚMERO INVÁLIDO.\033[m Qual vai ser seu ataque? [4 - rever os ataques] '))
            if ataque == 0 or ataque == 1 or ataque == 2 or ataque == 3:
                while limites_ven[ataque] == 0:
                    ataque = int(input('\033[1;31mLIMITE ZERADO\033[m. Escolha outro ataque: [4 - rever os ataques] '))
                    ataque = funções.ataque_4(ataque, venusaur_ataques)
            sleep(0.7)
            print(f'Você ativou o ataque {keys_ven[ataque]}, que da {values_ven[ataque]} de dano, você pode utiliza-lo {limites_ven[ataque]-1} vezes')
            limites_ven[ataque] -= 1
            sleep(0.7)
            print(f'O Rayquaza agora está com \033[1;31m{funções.vida(vida_rayquaza, values_ven[ataque])}\033[m de vida')
            vida_rayquaza = funções.vida(vida_rayquaza, values_ven[ataque])
            if vida_rayquaza == 0:
                funções.linha()
                print(f'\033[1;92mPARABÉNS! VOCÊ VENCEU\033[m')
                break
            funções.linha()
            sleep(0.7)

            #jogadas do pc
            print(f'\033[1;92mVEZ DO RAYQUAZA\033[m')
            sleep(0.7)
            print(f'Rayquaza ativou o ataque {keys_ray[jogada_rayquaza]}, que da {values_ray[jogada_rayquaza]} de dano, com limite de {limites_ray[jogada_rayquaza]-1}')
            limites_ray[jogada_rayquaza] -= 1
            while limites_ray[jogada_rayquaza] == 0:
                jogada_rayquaza = randint(0, 3)
            sleep(0.7)
            print(f'Agora o Venusaur está com \033[1;31m{funções.vida(vida_venusaur, values_ray[jogada_rayquaza])}\033[m de vida')
            vida_venusaur = funções.vida(vida_venusaur, values_ray[jogada_rayquaza])
            if vida_venusaur == 0:
                funções.linha()
                print(f'\033[1;31mVOCÊ PERDEU! :C\033[m')
                break
            sleep(0.7)

    continuar = input('Você gostaria de jogar novamente? [S/N] ').upper()
    while continuar not in 'SN':
        continuar = input('Digita algo válido, meu bom :). Você quer continuar? [S/N] ').upper()
    if continuar == 'N':
        break
funções.linha()
print('OBRIGADO POR TER JOGADO :D')