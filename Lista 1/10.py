"""  Faça um programa que receba uma letra e mostre se ela é
 uma vogal ou consoante """

letra = input("digite uma letra: ").lower()
vogal = ['a', 'e', 'i', 'o', 'u']

if letra in vogal:
    print("ela é uma vogal")
else:
    print("ela é uma consoante")