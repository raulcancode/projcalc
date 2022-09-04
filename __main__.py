# Programa Calculadora
# Requisitos: Lê dois números digitados pelo usuário, realiza operação
# aritmética definida pelo usuário, coloca o resultado na tela
# Data: 04/09/2022
# Versão 0.0.1



## Módulo principal programa calculadora



# Execução do programa


from __entrada__ import entra_dados
from __entrada__ import op_aritmetica
from __aritmetico__ import soma
from __aritmetico__ import subtracao
from __aritmetico__ import divisao
from __aritmetico__ import multiplicacao
from __saida__ import impressora



def main ():
    # Entrada
    lista = entra_dados()
    operacao = op_aritmetica()

    # Processamento
    if operacao == "+":
        resultado = soma(lista[0], lista[1])
    if operacao == "-":
        resultado = subtracao(lista[0], lista[1])
    if operacao == "*":
        resultado = multiplicacao(lista[0], lista[1])
    if operacao == "/":
        resultado = divisao(lista[0], lista[1])


    #Saída
    impressora(resultado, operacao, lista[0], lista[1])

if(__name__ == "__main__"):
    main()
