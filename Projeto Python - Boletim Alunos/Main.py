#Projeto em python - Boletim de alunos
from Módulos.Funções import f_incluir, f_menu, f_excluir, f_alterar, f_consultamedia, f_aprovado, f_gravar, f_recuperar
import json
turma = {
    '001': {'nome': '', 'Turma': 'DEV', 'Notas': ''},
    '002': {'nome': '', 'Turma': 'FOT', 'Notas': ''},
    '003': {'nome': '', 'Turma': 'DES', 'Notas': ''},
    '004': {'nome': '', 'Turma': 'MKT', 'Notas': ''},
    '005': {'nome': '', 'Turma': 'FMM', 'Notas': ''},
}

lista_alunos = []
lista_notas = []
lista_copia = []
x = 0
f_menu()

while True:

    menu = str(input('''Selecione uma opção:
    1. Incluir aluno
    2. Excluir aluno
    3. Alterar (sobrepor) notas do aluno
    4. Consultar notas e médias de aluno 
    5. Consultar lista de médias e aprovações da turma
    6. Salvar backup dos dados
    7. Recuperar backup dos dados
    8. Encerrar aplicação
    '''))

    if menu == '6':
        print('Gravando os dados...')
        f_gravar(turma)
        print('Concluído!')
        continue

    if menu == '7':
        print('Recuperando dados salvos...')
        turma = f_recuperar()
        print('Concluído!')
        continue

    if menu == '8':
        print('Encerrando o programa...')
        break

    while (x != '001' and x != '002' and x != '003' and x != '004' and x != '005'):
        opt = str(input('''Selecione a turma que deseja editar:
        [001] <-- DEV
        [002] <-- FOTOGRAFIA
        [003] <-- DESIGN
        [004] <-- MARKETING
        [005] <-- FILM MAKER
        '''))
        x = opt
        if (x != '001' and x != '002' and x != '003' and x != '004' and x != '005'):
            print('Selecione uma opção válida!\n' )
    x = 0
    print('='*20)
    if menu == '1':
        a, b = f_incluir()
        if turma[opt]['nome'] == '' and turma[opt]['Notas'] == '':
            turma[opt]['nome'] = [turma[opt]['nome']]
            turma[opt]['nome'].append(a)
            turma[opt]['Notas'] = [turma[opt]['Notas']]
            turma[opt]['Notas'].append(b)
        else:
            turma[opt]['nome'].append(a)
            turma[opt]['Notas'].append(b)
        if '' in turma[opt]['nome']:
            turma[opt]['nome'].pop(0)
            turma[opt]['Notas'].pop(0)
            
    if menu == '2':
        f_excluir(turma, opt)
        turma[opt]['nome'] = [a]
        turma[opt]['Notas'] = [b]

    if menu == '3':
        turma[opt]['Notas'] = f_alterar(turma, opt)
    
    if menu == '4':
        a, b, c = f_consultamedia(turma, opt)
        print(f'''
        Aluno: {a}
        Notas: {b}
        Média: {c}\n''')
    
    if menu == '5':
        classe = turma[opt]['Turma']
        print(f' Turma {classe}\n')
        a = f_aprovado(turma, opt)
        for x in a:
            print(f'{x[0][0]} - Média: {x[0][1]} \t Situação: {x[1]} ')

