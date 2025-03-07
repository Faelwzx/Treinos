#ler número N e escreva ele ao contrário com while, trate-o como número 

n = int(input("Digite um número inteiro positivo: "))
n2 = 0
while n > 0:
    n2 = n2 * 10 + n % 10
    n = n // 10
print(n2)
