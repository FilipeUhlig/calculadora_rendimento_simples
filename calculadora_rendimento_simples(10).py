"""
Programa: Calculadora de rendimentos
Descrição: Este programa calcula os rendimentos de um capital.
Autor: Filipe
Data: 04/06/2023
Versão: 0.0.1
"""
#Atribuição de variáveis

#Entrada de dados
pv = int(input("Qual é o valor do capital incial? "))
i = int(input("Qual é a taxa de juros em %? "))
n = int(input("Qual é o prazo? "))

#Processamento de dados
j = (pv *(i/100) * n)
fv = (pv + j)

#Saida de dados
print(f"O valor capitalizado é de {fv}.")