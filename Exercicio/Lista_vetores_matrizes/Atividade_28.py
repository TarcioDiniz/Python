# Escreva um programa em Python para corrigir uma prova com 10 questões de
# múltipla escolha (a, b, c, d ou e), em uma turma com 15 alunos. Cada questão
# vale 1 ponto. Leia o gabarito apenas uma vez, e para cada aluno leia sua
# matricula (número inteiro) e suas respostas. Calcule e escreva para cada aluno:
# sua matrícula, suas respostas, e sua nota. OBS: utilizar matrizes na solução.

import random


def generateFeedback():
    listChoices = ['a', 'b', 'c', 'd', 'e']
    _feedback = []
    for i in range(10):
        _feedback.append(listChoices[random.randint(0, len(listChoices) - 1)])
    return _feedback


def checkFeedback(official_feedback, student_feedback):
    student_grade = 0
    for i in range(len(official_feedback)):
        if student_feedback[i] == official_feedback[i]:
            student_grade += 1
    return student_grade


feedback = generateFeedback()
print(feedback)
students = []
for i in range(1):
    students.append({
        'Matricula': int(input('Informe a matricula: ')),
        'Respostas': [input(f'Informe a {res + 1} resposta: ') for res in range(10)]
    })
for i in range(len(students)):
    print(f'Matricula: {students[i]["Matricula"]}',
          f'Rspostas: {students[i]["Respostas"]}',
          f'Nota: {checkFeedback(feedback, students[i]["Respostas"])}', sep='\n')

