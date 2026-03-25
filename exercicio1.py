# 1 - Faça um programa que leia nome e peso
# de várias pessoas, 
# guardando tudo em uma lista. No final, mostre:

#Quantas pessoas foram cadastradas.
#Uma listagem com as pessoas mais pesadas.
#Uma listagem com as pessoas mais leves.

pessoas = list()
maior = menor = 0

while True:

    nome = str(input('Qual seu nome? '))
    peso = float(input('Qual seu peso? '))
    pessoas.append([nome, peso])

    if len(pessoas) == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    resp = input('Quer continuar? [S/N] ').upper()
    if resp == 'N':

        break

print( f'Ao todo você cadastrou {len(pessoas)} pessoas')

print(f'O maior peso foi de {maior} KG. Pessos:', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=' ')
print(f'O menor peso foi de {menor} KG. Pessos:', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end=' ')