#preço livro com desconto

preço_livro = 24.95
desconto = 0.40
transportePrimeiro = 3.00
transporteAdicional = 0.75
quantidade = 60

preço = preço_livro * (1 - desconto) * quantidade + transportePrimeiro + transporteAdicional * (quantidade - 1)
print(preço)


