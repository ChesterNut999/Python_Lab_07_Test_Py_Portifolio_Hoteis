import csv
import os
import runpy
import struct
import time

import Py_01_GeraRelatorio
import Py_03_PesquisaAvancada
from app_utils.func_gera_registros_db import gera_lista_db

# VARS
escolha_menu2 = None
cadastro = None
consulta = None

# DIRETORIOS
dir_db_hoteis_aprovados = '/home/Maurilio/PycharmProjects/Python_Lab_07_Test_Py_Portifolio_Hoteis/app_resources/' \
                          'db_hoteis_aprovados.csv'
dir_db_hoteis_reprovados = '/home/Maurilio/PycharmProjects/Python_Lab_07_Test_Py_Portifolio_Hoteis/app_resources' \
                           '/db_hoteis_reprovados.csv'

# -----------------------------------------------------------------------------------------------
os.system('clear' or 'cls')

while True:
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

    # Se consulta ou cadastro
    if escolha_menu2 == 1:
        # A função devolve uma lista onde cada elemento será iterado no loop for
        db_registros_totais = gera_lista_db()

        # Se registro existir no DB
        consulta = input('\n DIGITE UM NOME DE HOTEL VÁLIDO: ')

        for i in range(len(db_registros_totais)):
            if consulta == db_registros_totais[i]:
                try:
                    cadastro = str.upper(input('\nHOTEL JÁ CADASTRADO.\n'
                                               'DESEJA ACESSAR O MÓDULO PESQUISA AVANÇADA? DIGITE S/N: '))

                except BaseException:
                    print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
                    continue

                if cadastro == "S":
                    break

                elif cadastro == "N":
                    print(('-' * 60) + "\nVocê será redirecionado ao menu principal! Aguarde...\n" + ('-' * 60))

                    time.sleep(3)
                    os.system('clear' or 'cls')

                    break

                else:
                    print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
                    continue

        if cadastro == "S":
            break

        if cadastro == "N":
            continue

        # Se registro não existir no DB
        print(('-' * 60) + '\n' + str(consulta) + " não está na Base de Dados.\n" + ('-' * 60))

        while True:
            try:
                novo_registro_dec = str.upper(input("\nDESEJA EFETUAR UM NOVO CADASTRO? DIGITE S/N: "))

            except BaseException:
                print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
                continue

            # -----------------------------------------------------------------------------------------------
            # Critérios de aceitação e cadastro de registros nas bases de dados correspondentes
            if novo_registro_dec == "S":
                novo_registro = []
                novo_registro.append(input("\nNOME DO HOTEL: "))  # indice 0
                novo_registro.append(input('NÍVEL DE ESTRELAS DE 1 A 5: '))  # indice 1 (parâmetro main)
                novo_registro.append(input('TELEFONE COM DDD: '))  # indice 2
                novo_registro.append(input('HOTEL POSSUI ACESSIBILIDADE? DIGITE S/N: '))  # indice 3 (parâmetro main)
                novo_registro.append(input('HOTEL POSSUI ÁREA DE LAZER? DIGITE S/N: '))  # indice 4
                novo_registro.append(input('HOTEL POSSIU ATIVIDADES RECREATIVAS? DIGITE S/N: '))  # indice 5

                print(('-' * 60) + "\nAnalisando e comparando com requisitos de aceitação. Aguarde...\n" + ('-' * 60))

                # Critérios de aprovação
                if int(novo_registro[1]) > 3 and novo_registro[3].upper() == "S":
                    print(novo_registro[0] + " está qualificado como apto.")

                    with open(dir_db_hoteis_aprovados, 'a', newline='', encoding='UTF-8') as db_hoteis_aprovados:
                        writer = csv.writer(db_hoteis_aprovados, delimiter=',')
                        writer.writerow(novo_registro)
                        db_hoteis_aprovados.close()

                        print(('-' * 60) + "\nCadastro realizado com sucesso!\n" + ('-' * 60))

                        time.sleep(3)
                        os.system('clear' or 'cls')

                    break

                # Critérios de reprovação
                elif int(novo_registro[1]) <= 3 and novo_registro[3].upper() == "N":
                    print(novo_registro[0] + " não está qualificado como apto.\n" + ('-' * 60))

                    desqualificado = input("\nDESEJA PROSSEGUIR COM O REGISTRO MESMO ASSIM? DIGITE S/N: ")

                    if desqualificado.upper() == "S":
                        with open(dir_db_hoteis_reprovados, 'a', newline='', encoding='UTF-8') as db_hoteis_reprovados:
                            writer = csv.writer(db_hoteis_reprovados, delimiter=',')
                            writer.writerow(novo_registro)
                            db_hoteis_reprovados.close()

                            print(('-' * 60) + "\nCadastro realizado com sucesso!\n" + ('-' * 60))

                            time.sleep(3)
                            os.system('clear' or 'cls')

                        break

                    elif desqualificado.upper() == "N":
                        print(('-' * 60) + "\nVocê será redirecionado ao menu de cadastro! Aguarde...\n" + ('-' * 60))

                        time.sleep(3)
                        os.system('clear' or 'cls')

                        continue

                # Senão atender a nenhuma das condições anteriores, reprovado
                else:
                    print(novo_registro[0] + " não está qualificado como apto.\n" + ('-' * 60))

                    desqualificado = input("\nDESEJA PROSSEGUIR COM O REGISTRO MESMO ASSIM? DIGITE S/N: ")

                    if desqualificado.upper() == "S":
                        with open(dir_db_hoteis_reprovados, 'a', newline='', encoding='UTF-8') as db_hoteis_reprovados:
                            writer = csv.writer(db_hoteis_reprovados, delimiter=',')
                            writer.writerow(novo_registro)
                            db_hoteis_reprovados.close()

                            print(('-' * 60) + "\nCadastro realizado com sucesso!\n" + ('-' * 60))

                            time.sleep(3)
                            os.system('clear' or 'cls')

                        continue

                    elif desqualificado.upper() == "N":
                        print(('-' * 60) + "\nVocê será redirecionado ao menu de cadastro! Aguarde...\n" + ('-' * 60))

                        time.sleep(3)
                        os.system('clear' or 'cls')

                        break

            elif novo_registro_dec == "N":
                print(('-' * 60) + "\nVocê será redirecionado ao menu principal! Aguarde...\n" + ('-' * 60))

                time.sleep(3)
                os.system('clear' or 'cls')

                break

            else:
                print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
                continue
            # -----------------------------------------------------------------------------------------------

    # Se voltar ou prosseguir para outros módulos
    elif escolha_menu2 == 2 or 3:
        break

    # Se escolha não existir
    else:
        print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
        time.sleep(3)
        os.system('clear' or 'cls')
        continue

# -----------------------------------------------------------------------------------------------
# Carregar e executa outros módulos
if escolha_menu2 == 2:
    print(('-' * 60) + '\nCarregando módulo Relatório! Aguarde...\n' + ('-' * 60))

    time.sleep(3)
    runpy.run_module(mod_name='Py_01_GeraRelatorio')

elif escolha_menu2 == 3 or cadastro == "S":
    print(('-' * 60) + '\nCarregando módulo Pesquisa Avançada! Aguarde...\n' + ('-' * 60))
    time.sleep(3)
    runpy.run_module(mod_name='Py_03_PesquisaAvancada')

