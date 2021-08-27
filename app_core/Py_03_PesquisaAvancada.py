import os
import runpy
import time

import Py_01_GeraRelatorio
import Py_02_ConsultaEcadastro

# VARS
escolha_menu3 = None

# -----------------------------------------------------------------------------------------------
os.system('clear' or 'cls')

while True:
    print('\n---------- BEM VINDO AO SISTEMA DE PORTIFÓLIO DE HOTÉIS ----------\n')

    print(('-'*60) + "\nMÓDULO PESQUISA AVANÇADA\n" + ('-'*60))

    try:
        escolha_menu3 = int(input("\nO QUE DESEJA FAZER AGORA?"
                                 "\n1 - Pesquisar hoteis por atributos (Ex.: Nome, Nível de estrelas, Acessibilidade)"
                                 "\n2 - Acessar Consulta e Cadastro"
                                 "\n3 - Acessar Relatorio"
                                 "\nDIGITE SUA ESCOLHA: "))

    except BaseException:
        print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
        continue

    # NÃO IMPLEMENTADO
    if escolha_menu3 == 1:
        continue

    else:
        break

# -----------------------------------------------------------------------------------------------
# Carregar e executa outros módulos
if escolha_menu3 == 2:
    print(('-' * 60) + '\nCarregando módulo Consulta e Cadastro! Aguarde...\n' + ('-' * 60))
    time.sleep(3)
    runpy.run_module(mod_name='Py_02_ConsultaEcadastro')

elif escolha_menu3 == 3:
    print(('-' * 60) + '\nCarregando módulo Relatório! Aguarde...\n' + ('-' * 60))
    time.sleep(3)
    runpy.run_module(mod_name='Py_01_GeraRelatorio')

