#2 -   Crie um programa onde o usuário possa digitar sete valores 
# numéricos e cadastre-os em uma lista única que mantenha separados 
# os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

valores_numericos = [[], []]

for c in range (1, 8):

    valor_numerico = int(input(f'Digite o {c}° valor númerico: '))

    if valor_numerico % 2 == 0:
        valores_numericos[0].append(valor_numerico)
    else:
        valores_numericos[1].append(valor_numerico)

valores_numericos[0].sort()
valores_numericos[1].sort()

print('#*' * 30)
print('RESULTADO')
print('#*' * 30)

print (f'Os valores númerico pares em ordem crescente são {valores_numericos[0]}')
print (f'Os valores númerico ímpares em ordem crescente são {valores_numericos[1]}')

