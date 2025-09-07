""" Faça um programa que receba um caractere e mostre na tela
 “MAIÚSCULO” se o caracter for maiúsculo ou "MINÚSCULO" se o
 caracter for minúsculo. Dica: Utilize funções Maiusc/Minusc ou Carac(Valores >= 65 e <= 90 são maiúsculos) """

caractere = input("Digite um caractere : ")

if len(caractere) != 1:
    print("digitou mais de 1 caractere")
else:
    valor_ascii = ord(caractere)


if valor_ascii >= 65 and valor_ascii <= 90:
    print("MAIUSCULO")
else:
    print("MINUSCULO")

