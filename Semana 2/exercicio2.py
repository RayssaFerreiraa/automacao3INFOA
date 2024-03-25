'''
Exercicio 2:
Crie um programa que lê do teclado a nota
e a quantidade de faltas de um aluno. O
programadeve imprimir reprovado, se:
A nota for menor que 6 ou se as presenças forem
menor do que 75 e a aprovado caso contrário.
'''
# Ler a nota e a quantidade de faltas do teclado
nota = float(input("Digite a nota do aluno: "))
faltas = int(input("Digite a quantidade de faltas do aluno: "))

# Verificar se o aluno está reprovado ou aprovado
if nota < 6 or faltas < 75:
    print("Reprovado")
else:
    print("Aprovado")
