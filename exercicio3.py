#3 - Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

#No final mostre a matriz na tela na formatação correta.


matriz = ([],[],[])

for c in range (1, 10):
    numero_matriz = int(input(f'Qual é o {c}° número da matriz '))
    if c <= 3:
        matriz[0].append(numero_matriz)
    elif c >= 4 and c <= 6:
        matriz[1].append(numero_matriz)
    else:
        matriz[2].append(numero_matriz)

print(matriz[0])
print(matriz[1])
print(matriz[2])
