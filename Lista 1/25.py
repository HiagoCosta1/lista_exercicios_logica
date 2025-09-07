""" Faça um programa que sorteie um número inteiro entre 0 e
 100 (utilize a função randI()). Se o número sorteado estiver
 entre 10 e 20, o programa deverá mostrar “ABACAXI”, caso
 contrário, se estiver entre 50 e 90, o programa deverá
 mostrar “MAMÃO”, caso contrário, o programa deverá mostrar
 “BETERRABA” """

import random

def sorteio(num):
    if num >= 10 and num <= 20:
        return "ABACAXI"
    elif num >= 50 and num <= 90:
        return "MAMÃO"
    else:
        return "BETERRABA"

numero = random.randint(1,100)
print(f"a palavra sorteada foi: {sorteio(numero)}")

