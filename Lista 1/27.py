"""  Faça um programa que receberá dois números inteiros, A e
 B, e um terceiro número inteiro, C. Se C estiver entre A e B,
 o programa deverá mostrar “OK”, caso contrário, “Não OK” """

a,b,c = map(int, input("digite 3 numeros inteiros: ").split())

if c >= a and c <= b:
    print("OK")
else:
    print("Não OK")

