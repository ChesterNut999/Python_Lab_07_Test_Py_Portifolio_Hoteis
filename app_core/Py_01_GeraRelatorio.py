import csv
import os
import runpy
import time

import Py_02_ConsultaEcadastro
import Py_03_PesquisaAvancada
from app_utils.func_gera_relatorio import gera_relatorio as func_gera_relatorio

# VARS
escolha_menu1 = None

# DIRETORIOS
dir_relatorio_cadastros = '/home/Maurilio/PycharmProjects/Python_Lab_07_Test_Py_Portifolio_Hoteis/app_resources/' \
                          'relatorio_cadastros.csv'

# ------------------------------------------------------------------------------------------------
os.system('clear' or 'cls')

while True:
    print('\n---------- BEM VINDO AO SISTEMA DE PORTIFÓLIO DE HOTÉIS ----------\n')

    print(('-' * 60) + "\nMÓDULO RELATÓRIO\n" + ('-' * 60))

    try:
        escolha_menu1 = int(input("\nO QUE DESEJA FAZER AGORA?"
                                 "\n1 - Gerar relatório de todos os registros"
                                 "\n2 - Acessar Consulta e Cadastro"
                                 "\n3 - Acessar Pesquisa Avançada"
                                 "\nDIGITE SUA ESCOLHA: "))

    except BaseException:
        print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
        continue

    if escolha_menu1 == 1:
        gera_relatorio = func_gera_relatorio()

        with open(dir_relatorio_cadastros, 'w', encoding='UTF-8', newline='') as relatorio_cadastros:
            for i in range(len(gera_relatorio)):
                csv_writer = csv.writer(relatorio_cadastros, delimiter=',')
                csv_writer.writerow(gera_relatorio[i])

        relatorio_cadastros.close()

        print(('-' * 60) + "\nRelatório de registros gerado com sucesso!\n" + ('-' * 60))

        time.sleep(3)
        os.system('clear' or 'cls')
        continue

    elif escolha_menu1 == 2 or 3:
        break

    else:
        print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
        time.sleep(3)
        os.system('clear' or 'cls')
        continue

# -----------------------------------------------------------------------------------------------
# Carregar e executa outros módulos
if escolha_menu1 == 2:
    print(('-' * 60) + '\nCarregando módulo Consulta e Cadastro! Aguarde...\n' + ('-' * 60))
    time.sleep(3)
    runpy.run_module(mod_name='Py_02_ConsultaEcadastro')

elif escolha_menu1 == 3:
    print(('-' * 60) + '\nCarregando módulo Pesquisa Avançada! Aguarde...\n' + ('-' * 60))
    time.sleep(3)
    runpy.run_module(mod_name='Py_03_PesquisaAvancada')
