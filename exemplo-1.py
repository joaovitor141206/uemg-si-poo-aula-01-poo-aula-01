# Programação Estruturada

nome = "Camiseta"
preco = 50.0

def aplicar_desconto(preco, desconto):
    return preco - (preco * desconto)

preco = aplicar_desconto(preco, 0.1)

print(nome, preco)
