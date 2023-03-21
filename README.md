# Jogo-rpg-humanos-lobos-goblins
 Algoritmo em Python que simule um jogo RPG com criaturas misticas 


Este código é um exemplo de jogo de RPG simples que apresenta alguns conceitos importantes de programação orientada a objetos em Python.<br><br>
Primeiro, é importado o módulo ‘random’, que é usado para gerar valores aleatórios usados na criação de instâncias das classes ‘SerVivo’, ‘Lobo’ e ‘Goblin’. Em seguida, é definida a classe ‘SerVivo’, que é a classe base para as outras classes.<br><br>
A classe ‘SerVivo’ possui um construtor ‘__init__()’ que inicializa três atributos: ‘vida’, ‘ataque’ e ‘defesa’. O valor de ‘vida’ é definido como 100, enquanto os valores de ‘ataque’ e ‘defesa’ são gerados aleatoriamente dentro do intervalo de 5 a 15. Além disso, a classe ‘SerVivo’ possui um método ‘atacar()’, que recebe como argumento outro objeto ‘SerVivo’ e calcula o dano causado pelo ataque subtraindo a defesa do objeto atacado do ataque do objeto atacante.<br><br>
Em seguida, são definidas as classes ‘Personagem’, ‘Lobo’ e ‘Goblin’, que herdam da classe ‘SerVivo’.<br><br>
A classe ‘Personagem’ é usada para criar instâncias de personagens jogáveis e recebe como argumento o nome do personagem. A classe ‘Lobo’ é usada para criar instâncias de lobos inimigos e recebe como argumento a força do lobo. A classe ‘Goblin’ é usada para criar instâncias de goblins inimigos e recebe como argumento a inteligência do goblin.<br><br>
Cada uma dessas classes redefine o método ‘atacar()’ da classe ‘SerVivo’ para ajustar o dano causado pelo ataque com base nas características específicas do objeto.<br><br>
No trecho final do código, são criados uma instância de ‘Personagem’, uma instância de ‘Lobo’ e uma instância de ‘Goblin’. Em seguida, é chamado o método ‘atacar()’ em cada objeto para simular o combate. Por fim, o estado atual de cada objeto é impresso na tela.<br><br>
Em resumo, o código apresentado é um exemplo simples e didático de como utilizar a orientação a objetos em um jogo de RPG simples em Python.
