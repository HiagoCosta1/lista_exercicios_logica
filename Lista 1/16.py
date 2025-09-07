""" Faça um programa que receba um número entre 0 e 10 e diga
 se ele é um número primo """

numero = int(input("Digite um número: "))

if numero > 1 and all(numero % i != 0 for i in range(2, int(numero**0.5) + 1)):
    print("O número é primo!!")
else:
    print("O número não é primo.")
