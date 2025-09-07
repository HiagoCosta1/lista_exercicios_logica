"""  Faça um programa que receba um dois números reais, peso e
 altura de uma pessoa, e:
 a) calcule seu IMC, onde IMC = peso / altura².
 b) Apresente na tela a mensagem da coluna “Faixa de Risco”
 caso o IMC for equivalente. """

def imc(peso, altura):
    IMC = peso / altura **2
    return IMC 

def faixa_risco(imc):
    if imc < 20:
        return "Abaixo do peso"
    elif imc >= 20 and imc <= 25:
        return "Normal"
    elif imc > 25 and imc <= 30:
        return "Excesso de peso"
    elif imc > 30 and imc <= 35:
        return "Obesidade"
    else:
        return "Obesidade mórbida"


n1,n2 = map(float , input("Digite seu peso e altura e descubra seu IMC: ").split())

resultado = imc(n1,n2)
print(f"seu imc é: {resultado:.2f} e sua faixa de risco é {faixa_risco(resultado)}")