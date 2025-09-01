""" Faça um programa que receba um número dia entre 1 e 7 e
 mostre o nome do dia da semana. """

dias = {
    1: "Domingo",
    2: "Segunda",
    3: "Terça",
    4: "Quarta",
    5: "Quinta",
    6: "Sexta",
    7: "Sábado"
}
numero = int(input("Digite um numero entre 1 e 7: "))

while numero not in range(1, 8):   
    print("Número inválido, tente novamente!")
    numero = int(input("Digite um número entre 1 e 7: "))

print(f"{dias[numero]}")