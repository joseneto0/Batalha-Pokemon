from time import sleep
class Pokemon:
    def __init__(self, nome, nivel, hp, atk, defe, speed, ataques, danoAtaques):
        self.nome = nome
        self.nivel = nivel
        self.hp = hp
        self.atk = atk
        self.defe = defe
        self.speed = speed
        self.ataques = ataques
        self.dano_ataques = danoAtaques

    def conta(self, atk, dano_atk):
        return ((2 * self.nivel // (5 + 2) * atk * dano_atk // self.defe) // 50) + 2
    
    def mostrar_ataques(self, ataques, dano):
        for i in range(len(ataques)):
            print(f'[{i+1}] - {ataques[i]} - {dano[i]} de dano'.center(15), flush=True)

    def mostrar_ataques(self):
        for i in range(len(self.ataques)):
            print(f'[{i+1}] - {self.ataques[i]} ~ {self.dano_ataques[i]} de dano'.center(15), flush=True)
            sleep(1)
    
    def decrementar_vida(self, v):
        self.hp -= v
        if self.hp < 0:
            self.hp = 0
        return self.hp
