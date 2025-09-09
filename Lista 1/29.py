"""  Faça um programa que recebe um mês (número inteiro), diga
 quantos dias aquele mês tem (mês 2 sempre terá 28 dias). """

def MesAno(mes):
    meses = {
        1: 31,
        2: 28,  
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if mes not in meses:
        return f"Mês invalido"
    else:
        return meses.get(mes)

mes = int(input("Digite o numero do mês e veja quantos dias ele tem: "))
print(MesAno(mes))