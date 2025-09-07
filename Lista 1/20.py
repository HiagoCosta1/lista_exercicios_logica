"""  Faça um programa que receba sua data de nascimento (dia,
 mês e ano) e diga quantos dias você viveu """


from datetime import date , datetime
aniversario = datetime.strptime(input("Digite a data do seu aniversario: "), "%d/%m/%Y").date()
today = date.today()
dias_vividos = (today - aniversario).days
print(f"{dias_vividos} dias!")

