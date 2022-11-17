import json

def f_menu():
    print('='*20)
    print('CADASTRO DE ALUNOS')
    print('='*20)

def f_incluir():
    aluno = str(input('Informe o nome do aluno que deseja adicionar à turma: '))
    notas = [(int(input('Informe uma nota '))) for x in range(3)]
    return aluno, notas

def f_excluir(algo: dict, palavra: str):
    '''lista = [x.lower() for x in lista]
    pesquisa = str(input('Informe o nome do aluno o qual deseja excluir da turma: ')).lower()
    busca = lista.index(pesquisa)'''
    alunos = [x.lower() for x in algo[palavra]['nome']]
    notas = algo[palavra]['Notas']
    pesquisa = str(input('Informe o nome do aluno o qual deseja excluir da turma: ')).lower()
    busca = alunos.index(pesquisa)
    alunos = algo[palavra]['nome']
    alunos.pop(busca)
    notas.pop(busca)
    return alunos, notas

def f_alterar(algo: dict, palavra: str):
    alunos = [x.lower() for x in algo[palavra]['nome']]
    notas = algo[palavra]['Notas']
    pesquisa = str(input('Informe o nome do aluno o qual deseja alterar a nota: ')).lower()
    busca = alunos.index(pesquisa)
    print(notas)
    while True:
        escolha = int(input(f'''Escolha a nota a qual deseja alterar:
        1 -> {notas[busca][0]}
        2 -> {notas[busca][1]}
        3 -> {notas[busca][2]} '''))
        if  (escolha == 1 or escolha == 2 or escolha == 3):
            break
        else:
            print('Selecione uma opção válida!')
    escolha-= 1
    nova_nota = int(input('Informe a nova nota: '))
    notas[busca][escolha] = nova_nota
    return notas

def f_consultamedia(algo: dict, palavra: str):
    alunos = [x.lower() for x in algo[palavra]['nome']]
    notas = algo[palavra]['Notas']
    pesquisa = str(input('Informe o nome do aluno o qual deseja consultar: ')).lower()
    busca = alunos.index(pesquisa)
    notas = notas[busca]
    media = 0
    for x in notas:
        media += x
    media = (media/3)
    alunos = algo[palavra]['nome']
    alunos = alunos[busca]
    return alunos, notas, media

def f_aprovado(algo: dict, palavra: str):
    alunos = algo[palavra]['nome']
    notas = algo[palavra]['Notas']
    lista_medias = []
    aprovacao = []
    for x in notas:
        media = 0
        for y in x:
            media += y
        lista_medias.append(media/3)

    for x in lista_medias:
        if x >= 7:
            aprovacao.append('Aprovado')
        else:
            aprovacao.append('Reprovado')

    lista_medias = [ '%.2f' % elem for elem in lista_medias ]
    lista_pre_final = list(zip(alunos, lista_medias))
    lista_final = list(zip(lista_pre_final, aprovacao))
    return lista_final

def f_gravar(dicionario: dict):
    with open('backup_alunos.json', 'w') as arquivo:
        json.dump(dicionario, arquivo)

def f_recuperar():
    with open('backup_alunos.json', 'r') as arquivo:
        dicionario = json.load(arquivo)
    return dicionario    

