"""  Faça um programa que receba dois números. Mostre “OK”
 somente se o primeiro número for ímpar e o segundo número não
 for maior que o primeiro. Caso contrário, mostre “Não OK”.
 """

def is_ok(n1,n2):
    if n1 % 2 != 0 and not n2 > n1:
        print("OK")
    else:
        print("Não OK")

n1, n2 = map(float, input("Digite 2 numeros: ").split())

is_ok(n1,n2)

