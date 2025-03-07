#usuario digita um número e com while imprime todos os divisores desse número até o usuario digitar 0

n = int(input("Digite um número inteiro positivo: "))
d = 1
while d <= n:
    if n % d == 0:
        print(d)
    d += 1
