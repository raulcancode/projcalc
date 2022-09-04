# Programa Calculadora
# Requisitos: Lê dois números digitados pelo usuário, realiza operação
# aritmética definida pelo usuário, coloca o resultado na tela
# Data: 04/09/2022
# Versão 0.0.1

## Módulo de entrada


# Essa função lê dois números digitados pelo usuário - Função de Entrada

def entra_dados():
    i = 0
    lista_numeros = []
    while i < 2:
        numero = float(input("\nDigite um número:  "))
        lista_numeros.append(numero)
        i+=1
    return lista_numeros

def op_aritmetica():
    operacao = input("\nDigite a operação desejada: \n+ para soma, \n - para subtração, \n / para divisão, \n* para multiplicação.")
    return operacao