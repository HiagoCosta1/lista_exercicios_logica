"""  Faça um programa que receba dois segmentos de reta e diga
 se eles possuem uma intersecção entre si. Um segmento de reta
 é definido por dois pontos (X,Y). """

def se_interceptam(p1, q1, p2, q2):
    # As coordenadas dos pontos
    x1, y1 = p1
    x2, y2 = q1
    x3, y3 = p2
    x4, y4 = q2

    denominador = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    if denominador == 0:
        return False
    
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominador
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / deno
    if 0 <= t <= 1 and 0 <= u <= 1:
        return True
    

p1 = (1, 1)
q1 = (10, 1)
p2 = (1, 2)
q2 = (10, 2)
if se_interceptam(p1, q1, p2, q2):
    print("Os segmentos se interceptam!")
else:
    print("Os segmentos não se interceptam!")

