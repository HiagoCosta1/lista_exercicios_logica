"""  Faça um programa que receba seu aniversário e uma data e
 mostre quantos anos você tem naquela data. """


from datetime import date , datetime

hoje = date.today()
data = datetime.strptime(input("Digite a data do seu aniversario: "), "%d/%m/%Y").date()
anos = hoje.year - data.year
print(anos)



# outra forma

from datetime import date

dia, mes, ano = map(int, input().split("/"))
data = date(ano,mes,dia)
hoje = date.today()

idade = hoje.year - data.year

print(idade)
