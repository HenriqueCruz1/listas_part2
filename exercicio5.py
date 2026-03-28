# 5 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#  O programa vai perguntar quantos jogos serão gerados e vai sortear
#  6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

jogos = []

jogos_gerados = int(input('Quantos jogos serão gerados? '))

for i in range(jogos_gerados):
    numeros_escolhidos = []

    while len(numeros_escolhidos)< 6:
        numero = randint(1, 60)
        if numero not in numeros_escolhidos:
            numeros_escolhidos.append(numero)

    numeros_escolhidos.sort()
    jogos.append(numeros_escolhidos)

for i, jogo in enumerate(jogos):
    print(f'Jogo {i +1}: {jogo}')