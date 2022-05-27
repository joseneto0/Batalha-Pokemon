def vida(vida, dano):
    vida -= dano
    if vida <= 0:
        vida = 0
    return vida


def ataque_4(ataque, ataques_pokemons):
    while ataque == 4:
        linha()
        for i, e in enumerate(ataques_pokemons):
            print(f'{i} - {e}: {ataques_pokemons[e]} de ataque')
        linha()
        ataque = int(input('Qual vai ser seu ataque? [4 - rever os ataques] '))
    return ataque


def linha():
    print('-=' * 20)