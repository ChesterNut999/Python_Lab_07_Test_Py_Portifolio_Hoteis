import os
import time

from Py_01_GeraRelatorio import py_01_GeraRelatorio as Py_01
from Py_02_ConsultaEcadastro import py_02_consulta as Py_02
from Py_03_PesquisaAvancada import py_03_PesquisaAvancada as Py_03

# VARS
escolha_menu1 = None
escolha_menu2 = None
escolha_menu3 = None
py_01_marcacao = True
py_02_marcacao = None
py_03_marcacao = None

if __name__ == '__main__':
    while True:
        # FLUXO DE DADOS 1
        if py_01_marcacao:
            while True:
                os.system('clear' or 'cls')

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
                    Py_01(escolha_menu1)
                    continue

                elif escolha_menu1 == 2:
                    print(('-' * 60) + '\nCarregando módulo Consulta e Cadastro! Aguarde...\n' + ('-' * 60))
                    time.sleep(3)
                    py_02_marcacao = True
                    py_03_marcacao = False
                    break

                elif escolha_menu1 == 3:
                    print(('-' * 60) + '\nCarregando módulo Pesquisa Avançada! Aguarde...\n' + ('-' * 60))
                    time.sleep(3)
                    py_03_marcacao = True
                    py_02_marcacao = False
                    break

                else:
                    print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
                    time.sleep(3)
                    continue

        # FLUXO DE DADOS 2
        if py_02_marcacao:
            while True:
                os.system('clear' or 'cls')

                print('\n---------- BEM VINDO AO SISTEMA DE PORTIFÓLIO DE HOTÉIS ----------\n')

                print(('-' * 60) + "\nMÓDULO CONSULTA E CADASTRO\n" + ('-' * 60))

                try:
                    escolha_menu2 = int(input("\nO QUE DESEJA FAZER AGORA?"
                                              "\n1 - Realizar consulta ou cadastro"
                                              "\n2 - Acessar Relatório"
                                              "\n3 - Acessar Pesquisa Avançada"
                                              "\nDIGITE SUA ESCOLHA: "))

                except BaseException:
                    print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
                    continue

                if escolha_menu2 == 1:
                    Py_02(escolha_menu2)

                    if Py_02 == "N":
                        continue

                    elif Py_02 == "S":
                        py_01_marcacao = False
                        py_03_marcacao = True
                        break

                elif escolha_menu2 == 2:
                    print(('-' * 60) + '\nCarregando módulo Relatório! Aguarde...\n' + ('-' * 60))
                    time.sleep(3)
                    py_01_marcacao = True
                    py_03_marcacao = False
                    break

                elif escolha_menu2 == 3:
                    print(('-' * 60) + '\nCarregando módulo Pesquisa Avançada! Aguarde...\n' + ('-' * 60))
                    time.sleep(3)
                    py_01_marcacao = False
                    py_03_marcacao = True
                    break

                else:
                    print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
                    time.sleep(3)
                    continue

        # FLUXO DE DADOS 3
        if py_03_marcacao:
            while True:
                os.system('clear' or 'cls')

                print('\n---------- BEM VINDO AO SISTEMA DE PORTIFÓLIO DE HOTÉIS ----------\n')

                print(('-' * 60) + "\nMÓDULO PESQUISA AVANÇADA\n" + ('-' * 60))

                try:
                    escolha_menu3 = int(input("\nO QUE DESEJA FAZER AGORA?"
                                              "\n1 - Pesquisar hoteis por atributos (Ex.: Nome, Nível de estrelas, Acessibilidade)"
                                              "\n2 - Acessar Consulta e Cadastro"
                                              "\n3 - Acessar Relatorio"
                                              "\nDIGITE SUA ESCOLHA: "))

                except BaseException:
                    print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
                    continue

                if escolha_menu3 == 1:
                    Py_03()
                    continue

                elif escolha_menu3 == 2:
                    print(('-' * 60) + '\nCarregando módulo Consulta e Cadastro! Aguarde...\n' + ('-' * 60))
                    time.sleep(3)
                    py_02_marcacao = True
                    py_01_marcacao = False
                    break

                elif escolha_menu3 == 3:
                    print(('-' * 60) + '\nCarregando módulo Relatório! Aguarde...\n' + ('-' * 60))
                    time.sleep(3)
                    py_01_marcacao = True
                    py_02_marcacao = False
                    break

                else:
                    print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
                    time.sleep(3)
                    continue
