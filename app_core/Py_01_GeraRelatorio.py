import csv
import os
import time

import Py_02_ConsultaEcadastro
import Py_03_PesquisaAvancada
from app_utils.func_gera_relatorio import gera_relatorio as func_gera_relatorio

# DIRETORIOS
dir_relatorio_cadastros = '/home/Maurilio/PycharmProjects/Python_Lab_07_Test_Py_Portifolio_Hoteis/app_resources/' \
                          'relatorio_cadastros.csv'

def py_01_GeraRelatorio(escolha_menu1):
    while True:
        if escolha_menu1 == 1:
            gera_relatorio = func_gera_relatorio()

            with open(dir_relatorio_cadastros, 'w', encoding='UTF-8', newline='') as relatorio_cadastros:
                for i in range(len(gera_relatorio)):
                    csv_writer = csv.writer(relatorio_cadastros, delimiter=',')
                    csv_writer.writerow(gera_relatorio[i])

            relatorio_cadastros.close()

            print(('-' * 60) + "\nRelatório de registros gerado com sucesso!\n" + ('-' * 60))

            time.sleep(3)
            os.system('clear') if os.name == 'posix' == 'posix' else os.system('cls')
            break

        elif escolha_menu1 == 2 or 3:
            break

        else:
            print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
            time.sleep(3)
            os.system('clear') if os.name == 'posix' == 'posix' else os.system('cls')
            continue