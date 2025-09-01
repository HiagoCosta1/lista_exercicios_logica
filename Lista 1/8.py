"""  A unidade do ovo custa R$ 3,50 cada. Porém, caso seja
 comprada a cartela com 10 ovos, a unidade custa R$ 2,50.
 Escreva
 um programa que leia o número de ovos
 comprados,  calcule  e  escreva  o valor total da compra. """


unidade = 3.50
cartela = 2.50
numero = int(input("Quantos ovos você vai comprar? "))
if numero < 10:
    valor = numero * unidade
    print(valor)
elif numero == 10:
    valor = cartela * numero
    print(valor)
else:
    cartela = 10*cartela
    restante = (numero - 10) * unidade
    soma = cartela + restante
    print(soma)


