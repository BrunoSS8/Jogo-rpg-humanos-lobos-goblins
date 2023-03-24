import random

class SerVivo:
    def __init__(self, pontos_vida, pontos_ataque):
        self.pontos_vida = pontos_vida
        self.pontos_ataque = pontos_ataque
    
    def atacar(self):
        return random.randint(1, self.pontos_ataque)
    
    def defender(self, dano):
        self.pontos_vida -= dano

class Monstro(SerVivo):
    def __init__(self, nome, pontos_vida, pontos_ataque):
        super().__init__(pontos_vida, pontos_ataque)
        self.nome = nome

class Lobo(Monstro):
    def __init__(self, tamanho, pontos_vida, pontos_ataque):
        nome = f"Lobo {tamanho}"
        super().__init__(nome, pontos_vida, pontos_ataque)
        self.forca = random.randint(1, pontos_ataque)

class Goblin(Monstro):
    def __init__(self, tamanho, pontos_vida, pontos_ataque):
        nome = f"Goblin {tamanho}"
        super().__init__(nome, pontos_vida, pontos_ataque)
        self.inteligencia = random.randint(1, pontos_ataque)

def batalhar(jogador, monstro):
    print(f"Jogador: {jogador.pontos_vida} HP | Monstro: {monstro.pontos_vida} HP")
    while jogador.pontos_vida > 0 and monstro.pontos_vida > 0:
        ataque_jogador = jogador.atacar()
        print(f"Jogador atacou o {monstro.nome} com {ataque_jogador} de dano!")
        monstro.defender(ataque_jogador)
        if monstro.pontos_vida <= 0:
            break
        ataque_monstro = monstro.atacar()
        print(f"{monstro.nome} atacou o jogador com {ataque_monstro} de dano!")
        jogador.defender(ataque_monstro)
    if jogador.pontos_vida <= 0:
        print("Você perdeu!")
    else:
        print(f"{monstro.nome} foi derrotado!")

# Exemplo de uso
print("Bem-vindo ao jogo RPG!")
tamanho_monstro = input("Escolha o tamanho do monstro (grande, médio ou pequeno): ")
if tamanho_monstro == "grande":
    pontos_vida_monstro = random.randint(20, 30)
    pontos_ataque_monstro = random.randint(5, 10)
elif tamanho_monstro == "médio":
    pontos_vida_monstro = random.randint(10, 20)
    pontos_ataque_monstro = random.randint(3, 7)
else:
    pontos_vida_monstro = random.randint(5, 10)
    pontos_ataque_monstro = random.randint(1, 5)
tipo_monstro = input("Escolha o tipo de monstro (lobo ou goblin): ")
if tipo_monstro == "lobo":
    monstro = Lobo(tamanho_monstro, pontos_vida_monstro, pontos_ataque_monstro)
elif tipo_monstro == "goblin":
    monstro = Goblin(tamanho_monstro, pontos_vida_monstro, pontos_ataque_monstro)
else:
    print("Tipo de monstro inválido!")
    exit()
    
print(f"Você está enfrentando um {monstro.nome} com {monstro.pontos_vida} HP e {monstro.pontos_ataque} pontos de ataque!")
pontos_vida_jogador = random.randint(30, 50)
pontos_ataque_jogador = random.randint(8, 12)
jogador = SerVivo(pontos_vida_jogador, pontos_ataque_jogador)

print(f"Você tem {jogador.pontos_vida} HP e {jogador.pontos_ataque} pontos de ataque!")
input("Pressione Enter para começar a batalha...")
batalhar(jogador, monstro)
