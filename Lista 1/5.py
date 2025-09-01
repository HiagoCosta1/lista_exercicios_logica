""" Faça um programa que receba um número. Caso seja negativo, o
 programa deve mostrar o número em sua forma positiva. Caso
 contrário, o programa deverá multiplicar este número por 100. """


numero = int(input("Digite um numero: "))
if numero < 0:
    print(abs(numero))
else:
    numero*100
    print("O numero foi multiplicado!!")