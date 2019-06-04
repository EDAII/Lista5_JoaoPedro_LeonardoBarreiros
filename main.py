from arvore import No
import sys
import os
from utils import insere_randomico
from gera_relatorio import gera_csv_resultado, plot_grafico
import time
import random
import pandas as pd
from random import randint
from arvore_rb import RedBlackTree

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. criar uma arvore avl")
    print("2. inserir um elemento na arvore avl")
    print("3. plota grafico de arvore avl")
    print("4. Gera csv com os tempos de ordenação")
    print("5. Sair")
    print(67 * "-")

def grafico_arvore(tempo_ordenacao,nome_algoritmo):
    for i in range(100,1100, 100):
        inicio_cronometagem = time.time()
        tamanho_vetor=100
        lista = random.sample(range(0,tamanho_vetor), tamanho_vetor)
        arvore = No(randint(0,1000))
        for j in range(0,tamanho_vetor,  1):
            arvore.insere(lista[j])
        fim_cronometragem = time.time()
        tempo_cronometragem = fim_cronometragem - inicio_cronometagem
        tempo_ordenacao[nome_algoritmo][i] = tempo_cronometragem
        insere_randomico(lista, 100)
     
def grafico_arvore_rb(tempo_ordenacao,nome_algoritmo):
    for i in range(100,1100, 100):
        inicio_cronometagem = time.time()
        tamanho_vetor=100
        lista = random.sample(range(0,tamanho_vetor), tamanho_vetor)
        arvore = RedBlackTree()
        for j in range(0,tamanho_vetor,  1):
            arvore.insert(lista[j])
        fim_cronometragem = time.time()
        tempo_cronometragem = fim_cronometragem - inicio_cronometagem
        tempo_ordenacao[nome_algoritmo][i] = tempo_cronometragem
        insere_randomico(lista, 100)


if __name__ == '__main__':
    loop=True
    tempo_ordenacao_python = {'arvore_avl': {1000: 0, 2000: 0,
                   3000: 0, 4000: 0, 5000: 0, 6000: 0,
                   7000: 0, 8000: 0, 9000: 0, 10000: 0},
                    'arvore_avl': {}, 'arvore_rb': {}}
    tempo_ordenacao_python['arvore_avl'].update(tempo_ordenacao_python['arvore_avl'])
    tempo_ordenacao_python['arvore_rb'].update(tempo_ordenacao_python['arvore_avl'])
while loop:
        print_menu()
        choice = input("Entre sua opcao [1-5]: ")
        if choice=='1':
            print("Opcao 1 foi escolhida")
            print("Para criar a arvore precisa-se de uma raiz")
            raiz = input("Digite a raiz desejada: ")
            x = No(raiz)
            x.imprimeArvore()
        elif choice=='2':
            print("Opcao 1 foi escolhida")
            no = input("Digite o nó que deseja inserir: ")
            x.insere(no)
            x.imprimeArvore()
        elif choice=='3':
            print("Opcao 5 foi escolhida")
            grafico_arvore(tempo_ordenacao_python,'arvore_avl')
            grafico_arvore(tempo_ordenacao_python,'arvore_rb')
            plot_grafico(tempo_ordenacao_python)
        elif choice=='4':
            print("Opcao 6 foi escolhida")
            grafico_arvore(tempo_ordenacao_python,'arvore_avl')
            grafico_arvore(tempo_ordenacao_python,'arvore_rb')
            gera_csv_resultado(tempo_ordenacao_python)
        elif choice=='5':
            print("Opcao 7 foi escolhida")
            print('Saindo....')
            loop=False
        else:
            input("Opcao incorreta. Aperte qualquer tecla para tentar novamente..")