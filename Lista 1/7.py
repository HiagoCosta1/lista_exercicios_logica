"""  Faça um programa que receba um número mes entre 1 e 12 e
 mostre quantos dias possui o mês digitado. """

mes = {
    1: 31,  # Janeiro
    2: 28,  # Fevereiro (29 em ano bissexto)
    3: 31,  # Março
    4: 30,  # Abril
    5: 31,  # Maio
    6: 30,  # Junho
    7: 31,  # Julho
    8: 31,  # Agosto
    9: 30,  # Setembro
    10: 31, # Outubro
    11: 30, # Novembro
    12: 31  # Dezembro
}

numero = int(input("digite um numero de 1 a 12: "))

while numero not in range(1,13):
    print("numero invalido, tente novamente!")
    numero = int(input("digite um numero de 1 a 12: "))

print(f"{mes[numero]}")

#if numero in mes:
#    dias = mes[numero]
#    print(f"{dias}")
# daria para usar o if junto, porem ficaria redundante já que o while garante que a entrada do numero correto
# depois que sair do while, o valor vai ser verdadeiro, então só printar depois. 