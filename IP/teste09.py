#Conversão dias horas e minutos e talves segundos

Dia = int(input("digite x dias: "))
hora = int(input("digite x horas: "))
Minuto = int(input("digite x minutos: "))
Segundo = int(input("digite x segundos:"))

Segundos_dia = Dia * 86400
Segundos_hora = hora * 3600
Segundos_Minuto = Minuto * 60

print(f"a conversão Dias é: {Segundos_dia}")
print(f"a conversão Horas é: {Segundos_hora}")
print(f"a conversão Minutos é: {Segundos_Minuto}")
print(f"a conversão Segundos é: {Segundo}")