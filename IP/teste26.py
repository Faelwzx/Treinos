#gerar número aléatorio entre 1 e 9 e pedir para o usuário adivinhar o número,
#diga se o número é muito alto ou muito baixo, ou se acertou,caso ele digite sair o programa encerra

import random
n = random.randint(1, 9)
print("Adivinhe o número entre 1 e 9")
while True:
    a = int(input("Digite um número inteiro positivo: "))
    if a == n:
        print("Você acertou!")
        break
    elif a < n:
        print("Muito baixo")
    else:
        print("Muito alto")
    if a == 0:
        break

