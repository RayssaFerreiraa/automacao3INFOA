'''
Exercicio 1:

Crie um programa que lê dois números
inteiros do teclado e após imprime o 
maior númerodentre eles.
'''
# Ler os dois números inteiros do teclado
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Verificar qual número é maior
if numero1 > numero2:
    maior_numero = numero1
else:
    maior_numero = numero2

# Imprimir o maior número
print("O maior número é:", maior_numero)
