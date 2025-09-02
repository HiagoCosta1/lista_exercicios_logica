"""  Faça um programa que leia um ano e diga se ele é bissexto.
 """

def bissexto(ano):
    if ano % 400 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False


ano = int(input("Digite um ano: "))

print(bissexto(ano))