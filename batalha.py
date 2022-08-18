from pokemon import *
from time import sleep
from random import randint
print('-=' * 20)
print(f'{"BATALHA POKEMON":^40}')
print('-=' * 20)
#seu pokemon
poke1 = Pokemon('Foguinho da Galera', 100, 10, 100, 80, 100, ['Foguinho', 'Fogão', 'Bola de Fogo', 'Incẽndio Master'], [7, 9, 10, 12])
#inimigo
poke2 = Pokemon('Zezo Master', 100, 10, 90, 110, 70, ['Zezão Master', 'Zépelin', 'Zoubateu', 'ZegzZegz'], [10, 8, 7, 12])
print(f'{poke1.nome} x {poke2.nome}'.center(40))
while True:
    print('=' * 40)
    print(f'ATAQUES DE {poke1.nome}')
    poke1.mostrar_ataques(poke1.ataques, poke1.dano_ataques)
    escolha = int(input('Escolha seu ataque: '))
    escolha -= 1
    print('=' * 40)
    print(f'ATAQUES DE {poke2.nome}')
    poke1.mostrar_ataques(poke2.ataques, poke2.dano_ataques)
    ataque_inimigo = randint(0, 3)
    print(f'{poke2.nome} escolheu o ataque {poke2.ataques[ataque_inimigo]}')
    print()
    sleep(0.5)
    if poke1.speed > poke2.speed:
        dano = poke2.conta(poke1.atk, poke1.dano_ataques[escolha])
        print(f'O ataque de {poke1.nome} deu \033[1;31m{dano}\033[m em {poke2.nome}')
        vida = poke2.decrementar_vida(dano)
        sleep(0.5)
        print(f'Agora {poke2.nome} tem \033[1;31m{vida}\033[m de vida')
        if poke2.hp == 0:
            print(f'\033[1;92mVOCÊ GANHOU :D\033[m')
            break

        sleep(0.5)
        print('-' * 30)
        dano2 = poke1.conta(poke2.atk, poke2.dano_ataques[escolha])
        print(f'O ataque de {poke2.nome} deu \033[1;31m{dano2}\033[m em {poke1.nome}')
        sleep(0.5)
        vida2 = poke1.decrementar_vida(dano2)
        print(f'Agora {poke1.nome} tem \033[1;31m{vida2}\033[m de vida')
        if poke1.hp == 0:
            print(f'\033[1;31mVOCÊ PERDEU :C\033[m')
            break
    else:
        dano2 = poke1.conta(poke2.atk, poke2.dano_ataques[escolha])
        print(f'O ataque de {poke2.nome} deu \033[1;31m{dano2}\033[m em {poke1.nome}')
        sleep(0.5)
        vida2 = poke1.decrementar_vida(dano2)
        print(f'Agora {poke1.nome} tem \033[1;31m{vida2}\033[m de vida')
        sleep(0.5)
        if poke1.hp == 0:
            print(f'\033[1;31mVOCÊ PERDEU :C\033[m')
            break

        dano = poke2.conta(poke1.atk, poke1.dano_ataques[escolha])
        print(f'O ataque de {poke1.nome} deu \033[1;31m{dano}\033[m em {poke2.nome}')
        sleep(0.5)
        vida = poke2.decrementar_vida(dano)
        print(f'Agora {poke2.nome} tem \033[1;31m{vida}\033[m de vida')
        sleep(0.5)
        if poke2.hp == 0:
            print(f'\033[1;92mVOCÊ GANHOU :D\033[m')
            break
    sleep(1)