#Estrtura de repetição
##Executa uma instrução várias vezes

#For crescente
for i in range(0,10):
    print(i, "repetições")

 #For decrescente: range (inicio,fim-1,passo)
for i in range(10,-1,-2):
    print(i, "repetições decrescente")

#For com lista
lista_nomes =['Nathan', 
            'Gabriel',
            'Kaique',
            'Neymar']
for nome in lista_nomes:
     print(nome)

for index,nome in enumerate(lista_nomes):
     print(index, " -> ", nome)