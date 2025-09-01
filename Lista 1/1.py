""" Faça um programa que receba a idade de uma pessoa e mostre na
 tela “pode tirar habilitação” se a pessoa está apta ou “não
 pode tirar  habilitação” caso contrário """


print("Digite a sua idade: \n")
idade =  int(input())

if idade >= 18:
    print("Pode tirar habilitação")
else:
    print("Não pode tirar habilitação")
