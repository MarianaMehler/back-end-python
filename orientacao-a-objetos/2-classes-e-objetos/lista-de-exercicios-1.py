#Exercício 1

# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos(qualidades): ligado, cor, modelo, velocidade.
class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = 'preto'
        self.modelo = 'SUV'
        self.velocidade = 0
        self.velocidade_min = 5
        self.velocidade_max = 180

# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def acelerar(self):
        if not self.ligado:
            return
        
        if self.velocidade < self.velocidade_max:
            self.velocidade += 10

    def desacelerar(self):
        if not self.ligado:
            return
        
        if self.velocidade > self.velocidade_min:
            self.velocidade -= 10

    def __str__(self) -> str:
        return f'Ligado: {self.ligado} - cor: {self.cor} - modelo: {self.modelo} - velocidade: {self.velocidade}'

# Crie uma instância da classe carro.
meu_carro = Carro()
meu_carro.ligar()
print(f'meu_carro está ligado? {meu_carro.ligado}')

# Faça o carro "andar" utilizando os métodos da sua classe.
for _ in range(5):
    meu_carro.acelerar()

print(f'\nA velocidade do meu_carro andando é {meu_carro.velocidade}')
print()

# Faça o carro "parar" utilizando os métodos da sua classe.
for _ in range(2):
    meu_carro.desacelerar()

print(f'A velocidade do meu_carro parando é {meu_carro.velocidade}')
print()

print('meu_carro:', meu_carro)
print()