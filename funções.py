from time import sleep


def inicio(escolha, nome, vida_pokemons, ataques, limites):
    linha()
    print(f'\033[1;31mParabéns! Você escolheu o {nome[escolha - 1]}\033[m')
    sleep(1)
    print(f'O seu pokemon tem {vida_pokemons[escolha - 1]} de vida')
    sleep(1)
    for i, e in enumerate(ataques):
        print(f'{i} - {e}: {ataques[e]} de ataque, com limite de {limites[i]} vezes')
        sleep(1)
    linha()
    print("OH NÃO!")
    sleep(1)
    print("\033[1;32mUM RAYQUAZA APARECEU!\033[m")
    sleep(1)
    print("\033[1;31mLUTE PELA SUA VIDA, MESTRE POKEMON\033[m")
    sleep(1)
    print(f'O pokemon RAYQUAZA tem 70 de vida')


def vida(vida, dano):
    vida -= dano
    if vida <= 0:
        vida = 0
    return vida


def ataque(ataques_pokemons, limite=0):
    ataque = int(input('Qual vai ser seu ataque? [4 - rever os ataques] '))
    while ataque < 0 or ataque > 4:
        ataque = int(input('\033[1;31mNÚMERO INVÁLIDO.\033[m Qual vai ser seu ataque? [4 - rever os ataques] '))
    while ataque == 4:
        linha()
        for i, e in enumerate(ataques_pokemons):
            print(f'{i} - {e}: {ataques_pokemons[e]} de ataque')
        linha()
        ataque = int(input('Qual vai ser seu ataque? [4 - rever os ataques] '))
    if ataque == 0 or ataque == 1 or ataque == 2 or ataque == 3:
        while limite[ataque] == 0:
            ataque = int(input('\033[1;31mLIMITE ZERADO\033[m. Escolha outro ataque: [4 - rever os ataques] '))
            while ataque == 4:
                linha()
                for i, e in enumerate(ataques_pokemons):
                    print(f'{i} - {e}: {ataques_pokemons[e]} de ataque')
                linha()
                ataque = int(input('Qual vai ser seu ataque? [4 - rever os ataques] '))
    return ataque


def linha():
    print('-=' * 20)