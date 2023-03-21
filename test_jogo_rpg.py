from jogo_rpg import SerVivo, Personagem, Lobo, Goblin

# Criando personagem
p1 = Personagem('Klismann')

# Criando lobo com força 2
l1 = Lobo(2)

# Criando goblin com inteligência 3
g1 = Goblin(3)

# Personagem ataca lobo
p1.atacar(l1)

# Lobo ataca personagem
l1.atacar(p1)

# Goblin ataca lobo
g1.atacar(l1)

# Imprime estado dos personagens após ataques
print(f"{p1.nome} tem {p1.vida} pontos de vida.")
print(f"{l1.__class__.__name__} tem {l1.vida} pontos de vida.")
print(f"{g1.__class__.__name__} tem {g1.vida} pontos de vida.")
