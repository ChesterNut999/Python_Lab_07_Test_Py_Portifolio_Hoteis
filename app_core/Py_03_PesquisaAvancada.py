import os
import time
from app_utils.func_gera_registros_db import gera_lista_db

# DIRETORIOS
dir_db_hoteis_aprovados = '/home/Maurilio/PycharmProjects/Python_Lab_07_Test_Py_Portifolio_Hoteis/app_resources/' \
                              'db_hoteis_aprovados.csv'
dir_db_hoteis_reprovados = '/home/Maurilio/PycharmProjects/Python_Lab_07_Test_Py_Portifolio_Hoteis/app_resources' \
                               '/db_hoteis_reprovados.csv'

def py_03_PesquisaAvancada(escolha_menu3):
    # VARS
    global atributo
    global selecao

    while True:
        if escolha_menu3 == 1:
            try:
                atributo = int(input("\nESCOLHA UMA OPÇÃO DE ATRIBUTO PARA PESQUISAR:"
                               "\n1 - Nome do hotel"
                               "\n2 - Nível de estrelas"
                               "\n3 - Telefone com DDD"
                               "\n4 - Acessibilidade"
                               "\n5 - Aŕea de lazer"
                               "\n6 - Atividades Recreativas"
                               "\nDIGITE SUA ESCOLHA: "))

            except ValueError:
                print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
                time.sleep(3)
                continue

            if atributo == 1:
                selecao = str(input("\nDIGITE O NOME DO HOTEL: "))

                db_registros_totais = gera_lista_db()

                # for i in range(len(db_registros_totais)):
                #     if selecao == db_registros_totais[i]:
                #         print(("-"*60) + "\nRegistro encontrado:\n" + ("-"*60))
                #         print(db_registros_totais[i])
                #         break

                print(('-' * 60) + '\nConsulta realizada com sucesso!.\n' + ('-' * 60))
                time.sleep(5)

                break

            # elif atributo == 2:
            #
            # elif atributo == 3:
            #
            # elif atributo == 4:
            #
            # elif atributo == 5:
            #
            # elif atributo == 6:

            else:
                print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
                time.sleep(3)
                continue
