'''
Exercicio 2 - Semana 3:
Crie um programa que imprime usando
for a figura abaixo:
*
**
***
****
*****
******
termina com 10* na última linha
'''
# Definindo o número de linhas
num_linhas = 10

# Loop para imprimir as linhas
for i in range(1, num_linhas + 1):
    # Imprimir '*' repetidas vezes de acordo com o número da linha
    print('*' * i)

# Imprimir a última linha com 10 '*'
print('*' * 10)
