dic_alunos = {}
for vez in range(1,3,1):
    nome = input(f'Nome do aluno {vez}? ')
    notas=[]
    for i in range(1,5):
        nt = int(input(f'Nota {i} do aluno {nome}: '))
        notas.append(nt)
    
    chave_aluno = f'aluno{vez}'
    dic_alunos[chave_aluno] = {}
    dic_alunos[chave_aluno]['nome'] = nome
    dic_alunos[chave_aluno]['notas'] = notas
    dic_alunos[chave_aluno]['maior_nota'] = max(notas)
    dic_alunos[chave_aluno]['menor_nota'] = min(notas)
    dic_alunos[chave_aluno]['media_nota'] = sum(notas)/len(notas)
    if dic_alunos[chave_aluno]['media_nota'] >= 7:
        dic_alunos[chave_aluno]['situacao'] = 'Aprovado'
    else:
        dic_alunos[chave_aluno]['situacao'] = 'Reprovado'

for aluno in dic_alunos:
    print(aluno)
    print(dic_alunos[aluno])
    print('---------------------------------')

print('---------------------------------')
print('---------------------------------')
print(dic_alunos)

