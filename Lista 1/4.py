"""  Faça um programa que receba três números e mostre na tela o
 número de valor médio. """

def media(n1,n2,n3):
    numeros = [n1,n2,n3]
    soma = n1+n2+n3
    media = soma / len(numeros)
    return media

n1,n2,n3 = map(int, input("Digite 3 numeros: ").split())
resultado  = media(n1,n2,n3)
print(f"{resultado:.2f}")


