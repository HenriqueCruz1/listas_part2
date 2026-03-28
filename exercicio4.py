# 4 - Aprimore o desafio anterior, mostrando no final:
# A soma de todos os valores pares digitados.
# A soma de todos os valores da terceira coluna.
# O maior valor da segunda linha.

matriz = ([],[],[])
soma_pares = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = 0

for c in range (1, 10):
    numero_matriz = int(input(f'Qual é o {c}° número da matriz '))

    if numero_matriz % 2 == 0:
            soma_pares += numero_matriz

    if c <= 3:
        matriz[0].append(numero_matriz)
    elif c >= 4 and c <= 6:
        matriz[1].append(numero_matriz)
    else:
        matriz[2].append(numero_matriz)

for linha in matriz:
     soma_terceira_coluna += linha[2]

maior_valor_segunda_linha = max(matriz[1])

print(matriz[0])
print(matriz[1])
print(matriz[2])
print(f'A soma dos números pares da matriz é: {soma_pares}')
print(f'A soma da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é : {maior_valor_segunda_linha}')