""" Faça um programa que receba quatro valores e mostre a
 diferença entre o maior valor e o menor valor. """

def maior_menor(n1,n2,n3,n4):
    valores = [n1,n2,n3,n4]
    maior = valores[0]
    menor = valores[0]
    for i in valores:
        if i > maior:
            maior = i
        if i < menor:
            menor = i
        
    return maior, menor        

n1,n2,n3,n4 = map(float , input("digite 4 valores: ").split())

maior, menor = maior_menor(n1,n2,n3,n4)
print(f"{maior} {menor}")
