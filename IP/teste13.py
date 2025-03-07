# matar o fumante

CDias = int(input("cigarros por dia: "))

CAnos = int(input("cigarros por anos: "))

Tempo_vida = CDias * CAnos * 365

Tempo_restante = Tempo_vida * 30

tempo_para_morrer = Tempo_restante / 1440

print(f"morte em: {tempo_para_morrer}")