# Programação Orientada a Objetos

class Produto:
    def __init__(self, nome, preco, peso):
        self.nome = nome
        self.preco = preco
        self.peso = peso
    
    def aplicar_desconto(self, desconto):
        self.preco = self.preco - (self.preco * desconto)

    def calcular_frete(self):
        return self.peso * 10.0

p = Produto("Camiseta", 50.0, 0.2)
p.aplicar_desconto(0.1)
print(p.nome, p.preco, p.calcular_frete())

p2 = Produto("Calça Jeans", 90.0, 0.5)
p2.aplicar_desconto(0.1)
print(p2.nome, p2.preco, p2.calcular_frete())