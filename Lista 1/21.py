"""  Faça um programa que receba três números a, b, c, e calcule
 as raízes de uma equação de segundo grau ax²+bx+c """

import math

def form(a,b,c):
    D = b**2 - 4*a*c
    if D < 0:
        print("Não tem solução real!")
    elif D == 0:
        x = (-b)/2*a
        print(x)
    else:
        x1 = ((-b) + math.sqrt(D)) / 2*a
        x2 = ((-b) - math.sqrt(D)) / 2*a
        print(f"x1 = {x1} , x2 = {x2}")

a,b,c = map(float, input("digite 3 numeros para descobrir as raizes: ").split())

print(form(a,b,c))