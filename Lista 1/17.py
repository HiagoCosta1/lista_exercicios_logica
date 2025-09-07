"""  Faça um programa que receba dois números e mostre o menor
 seguido do maior """

a,b = map(float, input("Digite 2 numeros: ").split())

if a < b:
    print(f"{a} {b}")
else:
    print(f"{b} {a}")

# 

print(min(a,b), max(a,b))