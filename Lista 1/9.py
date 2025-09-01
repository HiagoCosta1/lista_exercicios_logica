""" Faça um programa que receba uma cadeia de caracteres e que
 siga as seguintes regras:
 a) Se for digitado “pt”, mostre na tela “Olá Mundo!”
 b) Se for digitado “en”, mostre na tela “Hello World!"
 c) Se for digitado “de”, mostre na tela “Hallow Wereld!”
 d) Se for digitado “jp”, mostre na tela “Konnichiha Sekai!”
 e) Se for digitado “es”, mostre “Hola Mundo! """

linguas = {
    'pt': "Olá Mundo!",
    'en': "Hello World!",
    'de': "Hallow Wereld!",
    'jp': "Konnichiha Sekai!",
    'es': "Hola Mundo!"
}

letra = input("digite uma tradução: ").lower()
if letra in linguas:
    print(linguas[letra])
else:
    print("Tradução não encontrada!")