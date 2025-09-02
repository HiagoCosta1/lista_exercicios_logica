""" Faça um programa que receba o centro de um círculo (x,y),
 o seu raio e as coordenadas de um ponto (x,y) e diga se o
 ponto está contido no círculo. 
 É dito que um ponto está dentro do círculo se a distância entre entre este ponto e o
 centro do círculo for menor que o seu raio. """

import math

xc,yc= map(float, input("Digite a coordenada x e y do centro do círculo: ").split())

raio = float(input("Digite o raio do círculo: "))

xp, yp= map(float, input("Digite a coordenada x e y do ponto: ").split())

distancia = math.sqrt((xp - xc) ** 2 + (yp - yc) ** 2)

if distancia < raio:
    print("O ponto está dentro do círculo.")
elif distancia == raio:
    print("O ponto está na borda do círculo.")
else:
    print("O ponto está fora do círculo.")
