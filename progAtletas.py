atletas = { 'nome': [],
           'categoria': [],
           'lutas': [],
           'vitorias': [],
           'derrotas': []        
}





while True:
    atletas['nome'].append(input('Digite o nome: '))
   
    atletas['categoria'].append(float(input('Digite o categoria: ')))

    atletas['lutas'].append(int(input('Total de lutas: ')))

    atletas['vitorias'].append(int(input('Total de vitorias: ')))

    atletas['derrotas'].append(int(input('Total de derrotas: ')))

    op = input('Deseja inserir outro lutador.(S/N)')
    if op.upper() == 'N':
        break
    else:
        continue
for key,value in atletas.items():
    print(key)
    print(value)