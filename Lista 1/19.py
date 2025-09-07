"""  Faça um programa que receba um ponto A (x,y), um ponto B
 (x,y) e um ponto C (x,y) e diga se o ponto C está entre o
 ponto A e B """

def esta_entre(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    colinear = (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1)

    dentro = (min(x1, x2) <= x3 <= max(x1, x2)) and (min(y1, y2) <= y3 <= max(y1, y2))

    return colinear and dentro

x1, y1 = map(int, input("Digite as coordenadas de A (x y): ").split())
x2, y2 = map(int, input("Digite as coordenadas de B (x y): ").split())
x3, y3 = map(int, input("Digite as coordenadas de C (x y): ").split())

if esta_entre((x1, y1), (x2, y2), (x3, y3)):
    print("O ponto C está entre A e B.")
else:
    print("O ponto C NÃO está entre A e B.")
