# 6 -  Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

boletim = []

while True:

    nome = input('Qual o nome do aluno ? ')
    nota_1 = float(input('Qual o valor da primeira nota? '))
    nota_2 = float(input('Qual o valor da segunda nota? '))
    media = (nota_1 + nota_2 ) / 2

    boletim.append([nome, nota_1, nota_2, media])

    pergunta = input('Deseja cadastrar mais alunos? [S/N]').upper()
    while pergunta not in 'SN':
        print('Resposta invalida. Digite S ou N')
    if pergunta == 'N':
        break

print('\nBoletim:')
print('Nº  Nome       Média')
for i, aluno in enumerate(boletim,start = 1):
    print(f'{i}   {aluno[0]}       {aluno[3]:.1f}')

# Ver notas individuais
while True:
    opcao = int(input('\nMostrar notas de qual aluno? (999 para sair) '))
    if opcao == 999:
        break
    if 1 <= opcao <= len(boletim):
        print(f'Notas de {boletim[opcao-1][0]}: {boletim[opcao-1][1:3]}')

    
