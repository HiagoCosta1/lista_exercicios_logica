"""  Faça um programa que receba dois valores diferentes de
 zero e mostre se o primeiro valor é divisível pelo segundo
 valor. Caso um dos valores seja igual a zero, o programa deve
 mostrar a mensagem “Um dos valores é zero!” e não executar
 nenhuma operação """

def e_div(a,b):
    if a == 0 or b == 0:
        return "Um dos valores é zero!"
    elif a % b == 0:
        return "é divisivel!"
    else:
        return "Não é divisivel!"
        
a,b = map(float, input("Digite 2 valores diferentes de 0: ").split())
print(e_div(a,b))