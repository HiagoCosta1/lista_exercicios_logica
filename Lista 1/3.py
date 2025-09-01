""" Faça um programa que receba três números e mostre na tela o
 maior deles. """

n1,n2,n3 = map(int, input("Digite 3 numeros: ").split())
lista = []
lista.extend([n1,n2,n3])
print(max(lista))


#comparar os 3 com if e ver quem é maior (obvio)
#criar uma lista e puxar o maior