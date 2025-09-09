"""  Faça um programa que receba dois números, Horas e Minutos,
 e diga se está de dia (até 12h) ou de noite (até 24h). Caso
 minutos seja maior que 60 ou menor que 0, e horas maior que
24 ou menor que zero, o programa deverá mostrar que o horário
 está inválido """


def isdia_noite(hora, minuto):
    if (hora >= 24 or hora < 0) or (minuto > 59 or minuto < 0):
        return "esta invalido"

    if hora <= 12:
        return "é dia"
    else:
        return "é noite"
    
try:
    hora, minuto = map(int, input("Digite Horas e Minutos: ").split())
    print(isdia_noite(hora, minuto))
except ValueError:
    print("Entrada inválida. Digite apenas números inteiros.")

