""" Faça um programa que receba o nome de um dia da semana e
 mostre se ele é final de semana ou não. """


semana = ['segunda', 'terca', 'quarta', 'quinta', 'sexta']
dia = input("Digite um dia da semana: ").lower()

if dia  in semana:
    print("é dia de semana!!")
else:
    print("é final de semana!!")
