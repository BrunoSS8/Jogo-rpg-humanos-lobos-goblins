import random

class SerVivo:
    def __init__(self):
        self.vida = 100
        self.ataque = random.randint(5, 15)
        self.defesa = random.randint(5, 15)

    def atacar(self, outro):
        dano = self.ataque - outro.defesa
        if dano > 0:
            outro.vida -= dano
            print(f"{self.__class__.__name__} causou {dano} pontos de dano em {outro.__class__.__name__}")
        else:
            print(f"{self.__class__.__name__} não causou dano em {outro.__class__.__name__}")

class Personagem(SerVivo):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome

class Lobo(SerVivo):
    def __init__(self, forca):
        super().__init__()
        self.forca = forca

    def atacar(self, outro):
        dano = self.ataque * self.forca - outro.defesa
        if dano > 0:
            outro.vida -= dano
            print(f"{self.__class__.__name__} causou {dano} pontos de dano em {outro.__class__.__name__}")
        else:
            print(f"{self.__class__.__name__} não causou dano em {outro.__class__.__name__}")

class Goblin(SerVivo):
    def __init__(self, inteligencia):
        super().__init__()
        self.inteligencia = inteligencia

    def atacar(self, outro):
        dano = self.ataque + self.inteligencia - outro.defesa
        if dano > 0:
            outro.vida -= dano
            print(f"{self.__class__.__name__} causou {dano} pontos de dano em {outro.__class__.__name__}")
        else:
            print(f"{self.__class__.__name__} não causou dano em {outro.__class__.__name__}")
