#ler números digitados pelo usuário ,ate que o número seja 0 e imprimir a soma deles

soma = 0
n = int(input("Digite um número inteiro positivo: "))
while n != 0:
    soma += n
    n = int(input("Digite um número inteiro positivo: "))
print(soma)