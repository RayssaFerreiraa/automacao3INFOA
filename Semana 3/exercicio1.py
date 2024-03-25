'''
Exercicio 1 - Semana 3:
Crie um programa que imprime todos os
números pares no intervalo de 0 a 20.
'''
# Loop para iterar sobre os números de 0 a 20
for numero in range(0, 21):
    # Verificar se o número é par
    if numero % 2 == 0:
        print(numero)
