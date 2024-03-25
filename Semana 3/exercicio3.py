'''
Exercicio 3 - Semana 3:
Crie um programa que lê do teclado
sucessivos números de matricula(int).
O programa deve parar de ler os números quando a
matricula 0 for digitada.
Ao final deve apresentar os números de matriculas
separados em 3 grupos.
'''
# Listas para armazenar os números de matrícula
grupo1 = []
grupo2 = []
grupo3 = []

# Loop para ler os números de matrícula
while True:
    matricula = int(input("Digite o número da matrícula (digite 0 para parar): "))
    
    # Verificar se o número de matrícula é 0 para parar
    if matricula == 0:
        break
    
    # Adicionar a matrícula ao grupo correspondente
    if len(grupo1) < 3:
        grupo1.append(matricula)
    elif len(grupo2) < 3:
        grupo2.append(matricula)
    else:
        grupo3.append(matricula)

# Imprimir os grupos
print("Grupo 1:", grupo1)
print("Grupo 2:", grupo2)
print("Grupo 3:", grupo3)
