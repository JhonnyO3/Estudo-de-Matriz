# Creating a list of lists.
#Exemplo sem o uso de listas
aluno_0_0, aluno_0_1, aluno_0_2 = 5.5, 7.0, 8.7
aluno_1_0, aluno_1_1, aluno_1_2 = 8.0, 6.0, 9.2
aluno_2_0, aluno_2_1, aluno_2_2 = 7.0, 8.0, 2.2
aluno_3_0, aluno_3_1, aluno_3_2 = 10.0, 5.0, 6.2

#Exemplo com o uso de listas
aluno_0 = [5.5, 7.0, 8.7]
aluno_1 = [8.0, 6.0, 9.2]
aluno_2 = [7.0, 8.0, 2.2]
aluno_3 = [10.0, 5.0, 6.2]

# Creating a list of lists.
#Exemplo com o uso de matriz (array de arrays)
alunos = [aluno_0, aluno_1, aluno_2, aluno_3]


def coleta_notas():
    notas = input("Digite a nota").split()
    for i in range(len(notas)):
        n = float(notas[i])
        notas.append(n)
    return notas

def preencher_turma(qtde_alunos):
    turma = []
    for i in range(qtde_alunos):
        print(f'{i + 1}º aluno: /n')
        aluno = coleta_notas()
        turma.append(aluno)
    return turma

def calcular_media(aluno):
    soma = 0
    for nota in aluno:
        soma += nota
    return soma / len(aluno)

def resumo_turma(turma):
    for aluno in turma:

