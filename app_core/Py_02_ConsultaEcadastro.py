import csv
import os
import time
from app_utils.func_gera_registros_db import gera_lista_db

# DIRETORIOS
dir_db_hoteis_aprovados = '/home/Maurilio/PycharmProjects/Python_Lab_07_Test_Py_Portifolio_Hoteis/app_resources/' \
                              'db_hoteis_aprovados.csv'
dir_db_hoteis_reprovados = '/home/Maurilio/PycharmProjects/Python_Lab_07_Test_Py_Portifolio_Hoteis/app_resources' \
                               '/db_hoteis_reprovados.csv'

# Consulta
def py_02_consulta(escolha_menu2):
    while True:
        # Se consulta ou cadastro
        if escolha_menu2 == 1:
            # A função devolve uma lista onde cada elemento será iterado no loop for
            db_registros_totais = gera_lista_db()

            # Se está ou não contido no DB
            consulta = str(input('\nDIGITE UM NOME DE HOTEL VÁLIDO: '))

            for i in range(len(db_registros_totais)):
                if consulta == db_registros_totais[i]:
                    print('HOTEL JÁ CADASTRADO.')
                    print(('-' * 60) + "\nVocê será redirecionado ao menu principal! Aguarde...\n" + ('-' * 60))
                    time.sleep(3)
                    break

            if consulta not in db_registros_totais:
                py_02_cadastro()
                break

            if consulta in db_registros_totais:
                break

        # Se voltar ou prosseguir para outros módulos
        elif escolha_menu2 == 2 or 3:
            break

        # Se escolha não existir
        else:
            print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
            time.sleep(3)
            continue

# Se registro não existir no DB
def py_02_cadastro():
    # VARS
    consulta = None

    print(('-' * 60) + '\n' + str(consulta) + " não está na Base de Dados.\n" + ('-' * 60))

    while True:
        try:
            novo_registro_dec = str.upper(input("\nDESEJA EFETUAR UM NOVO CADASTRO? DIGITE S/N: "))

        except BaseException:
            print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
            time.sleep(3)
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
                    os.system('clear') if os.name == 'posix' == 'posix' else os.system('cls')

                break

            # Critérios de reprovação
            elif int(novo_registro[1]) <= 3 and novo_registro[3].upper() == "N":
                print(novo_registro[0] + " não está qualificado como apto.\n" + ('-' * 60))

                desqualificado = str.upper(input("\nDESEJA PROSSEGUIR COM O REGISTRO MESMO ASSIM? DIGITE S/N: "))

                if desqualificado == "S":
                    with open(dir_db_hoteis_reprovados, 'a', newline='', encoding='UTF-8') as db_hoteis_reprovados:
                        writer = csv.writer(db_hoteis_reprovados, delimiter=',')
                        writer.writerow(novo_registro)
                        db_hoteis_reprovados.close()

                        print(('-' * 60) + "\nCadastro realizado com sucesso!\n" + ('-' * 60))

                        time.sleep(3)
                        os.system('clear') if os.name == 'posix' == 'posix' else os.system('cls')

                    break

                elif desqualificado == "N":
                    print(('-' * 60) + "\nVocê será redirecionado ao menu de cadastro! Aguarde...\n" + ('-' * 60))
                    time.sleep(3)
                    os.system('clear') if os.name == 'posix' == 'posix' else os.system('cls')

                    continue

            # Senão atender a nenhuma das condições anteriores, reprovado
            else:
                print(novo_registro[0] + " não está qualificado como apto.\n" + ('-' * 60))

                desqualificado = str.upper(input("\nDESEJA PROSSEGUIR COM O REGISTRO MESMO ASSIM? DIGITE S/N: "))

                if desqualificado == "S":
                    with open(dir_db_hoteis_reprovados, 'a', newline='', encoding='UTF-8') as db_hoteis_reprovados:
                        writer = csv.writer(db_hoteis_reprovados, delimiter=',')
                        writer.writerow(novo_registro)
                        db_hoteis_reprovados.close()

                        print(('-' * 60) + "\nCadastro realizado com sucesso!\n" + ('-' * 60))
                        time.sleep(3)
                        os.system('clear' or 'cls')
                    break

                elif desqualificado == "N":
                    print(('-' * 60) + "\nVocê será redirecionado ao menu de cadastro! Aguarde...\n" + ('-' * 60))
                    time.sleep(3)
                    os.system('clear') if os.name == 'posix' == 'posix' else os.system('cls')

                    break

        elif novo_registro_dec == "N":
            print(('-' * 60) + "\nVocê será redirecionado ao menu principal! Aguarde...\n" + ('-' * 60))
            time.sleep(3)

            break

        else:
            print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
            time.sleep(3)

            continue