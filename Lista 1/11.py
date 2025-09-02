"""  Faça um programa que receba duas notas e, se a média for
 menor que 7, mostre “reprovado”. Caso contrário, mostre
 “aprovado” """


n1, n2 = map(int, input("Digite 2 notas e receba a media: ").split())

soma = n1 + n2

if (soma / 2) < 7:
    print("Reprovado")
else:
    print("Aprovado")


