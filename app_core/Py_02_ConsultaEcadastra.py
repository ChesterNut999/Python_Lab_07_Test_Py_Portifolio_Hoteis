import csv
import runpy
import app_core.Py_03_FiltroDePesquisa as Py_03
from app_utils.func_gera_registros_db import gera_lista_db

# VARS
cadastro = None

print(('-'*60) + "\nMÓDULO CONSULTA E CADASTRO\n" + ('-'*60))

while True:
    consulta = str(input('\nCONSULTA E CADASTRO DE HOTEL. DIGITE UM NOME VÁLIDO: '))

    # Se registro vazio/nulo
    if consulta == "":
        print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
        continue

    # A função devolve uma lista onde cada elemento será iterado no loop for
    db_registros_totais = gera_lista_db()

    # Se registro existir no DB

    for i in range(len(db_registros_totais)):
        if consulta == db_registros_totais[i]:
            try:
                cadastro = str.upper(input('\nHOTEL JÁ CADASTRADO.\n'
                                     'DESEJA PROSSEGUIR PARA O MÓDULO DE PESQUISA DETALHADA? DIGITE S/N: '))

            except BaseException:
                print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
                continue

            if cadastro == "S":
                runpy.run_module(mod_name=Py_03)
                break

            elif cadastro == "N":
                print(('-' * 60) + "\nVocê será redirecionado ao menu principal! Aguarde...\n" + ('-' * 60))
                break

            else:
                print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
                continue

    if cadastro == "N":
        continue

    # Se registro não existir no DB
    print(('-' * 60) + '\n' + consulta + " não está na Base de Dados.\n" + ('-' * 60))

    while True:
        try:
            novo_registro_dec = str(input("\nDESEJA EFETUAR UM NOVO REGISTRO? DIGITE S/N: "))

        except BaseException:
            print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
            continue

        if novo_registro_dec.upper() == "S":
            novo_registro = []
            novo_registro.append(input("\nNOME DO HOTEL: "))  # indice 0
            novo_registro.append(input('NÍVEL DE ESTRELAS DE 1 A 5: '))  # indice 1 (parâmetro principal)
            novo_registro.append(input('TELEFONE COM DDD: '))  # indice 2
            novo_registro.append(input('HOTEL POSSUI ACESSIBILIDADE? DIGITE S/N: '))  # indice 3 (parâmetro principal)
            novo_registro.append(input('HOTEL POSSUI ÁREA DE LAZER? DIGITE S/N: '))  # indice 4
            novo_registro.append(input('HOTEL POSSIU ATIVIDADES RECREATIVAS? DIGITE S/N: '))  # indice 5

            print(('-' * 60) + "\nAnalisando e comparando com requisitos de aceitação. Aguarde...\n" + ('-' * 60))

            if int(novo_registro[1]) > 3 and novo_registro[3].upper() == "S":
                print(novo_registro[0] + " está qualificado como apto.")

                with open('../app_resources/db_hoteis_aprovados.csv', 'r', encoding='UTF-8') as db_hoteis_aprovados:
                    reader = csv.reader(db_hoteis_aprovados, delimiter=',')

                with open('../app_resources/db_hoteis_aprovados.csv', 'a', newline='', encoding='UTF-8') as db_hoteis_aprovados:
                    writer = csv.writer(db_hoteis_aprovados, delimiter=',')
                    writer.writerow(novo_registro)
                    db_hoteis_aprovados.close()

                    print(('-' * 60) + "\nCadastro realizado com sucesso!\n" + ('-' * 60))

                while True:
                    try:
                        mod_pesquisa = int(input("\nO QUE DESEJA FAZER AGORA?"
                                                 "\n1 - Voltar ao menu de cadastro"
                                                 "\n2 - Prosseguir para o módulo de pesquisa avançada"
                                                 "\nDIGITE SUA ESCOLHA: "))

                        print("-" * 60)

                    except BaseException:
                        print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + (
                                '-' * 60))
                        continue

                    if mod_pesquisa == 1:
                        break

                    elif mod_pesquisa == 2:
                        runpy.run_module(mod_name=Py_03)
                        break

                    else:
                        print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
                        continue

            elif int(novo_registro[1]) <= 3 and novo_registro[3].upper() == "N":
                print(novo_registro[0] + " não está qualificado como apto.\n" + ('-' * 60))

                desqualificado = input("\nDESEJA PROSSEGUIR COM O REGISTRO MESMO ASSIM? DIGITE S/N: ")

                if desqualificado.upper() == "S":
                    with open('../app_resources/db_hoteis_reprovados.csv', 'r',
                              encoding='UTF-8') as db_hoteis_reprovados:
                        reader = csv.reader(db_hoteis_reprovados, delimiter=',')

                    with open('../app_resources/db_hoteis_reprovados.csv', 'a', newline='',
                              encoding='UTF-8') as db_hoteis_reprovados:
                        writer = csv.writer(db_hoteis_reprovados, delimiter=',')
                        writer.writerow(novo_registro)
                        db_hoteis_reprovados.close()

                        print(('-' * 60) + "\nCadastro realizado com sucesso!\n" + ('-' * 60))

                    while True:
                        try:
                            mod_pesquisa = int(input("\nO QUE DESEJA FAZER AGORA?"
                                                     "\n1 - Voltar ao menu de cadastro"
                                                     "\n2 - Prosseguir para o módulo de pesquisa avançada"
                                                     "\nDIGITE SUA ESCOLHA: "))

                        except BaseException:
                            print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + (
                                    '-' * 60))
                            continue

                        if mod_pesquisa == 1:
                            print(('-' * 60) + "\nVocê será redirecionado ao menu de cadastro! Aguarde...\n" + (
                                    '-' * 60))
                            break

                        elif mod_pesquisa == 2:
                            runpy.run_module(mod_name=Py_03)
                            break

                        else:
                            print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + (
                                    '-' * 60))
                            continue

                elif desqualificado.upper() == "N":
                    print(
                        ('-' * 60) + "\nVocê será redirecionado ao menu de cadastro! Aguarde...\n" + ('-' * 60))
                    break

            else:
                print(novo_registro[0] + " não está qualificado como apto.\n" + ('-' * 60))

                desqualificado = input("\nDESEJA PROSSEGUIR COM O REGISTRO MESMO ASSIM? DIGITE S/N: ")

                if desqualificado.upper() == "S":
                    with open('../app_resources/db_hoteis_reprovados.csv', 'r',
                              encoding='UTF-8') as db_hoteis_reprovados:
                        reader = csv.reader(db_hoteis_reprovados, delimiter=',')

                    with open('../app_resources/db_hoteis_reprovados.csv', 'a', newline='',
                              encoding='UTF-8') as db_hoteis_reprovados:
                        writer = csv.writer(db_hoteis_reprovados, delimiter=',')
                        writer.writerow(novo_registro)
                        db_hoteis_reprovados.close()

                        print(('-' * 60) + "\nCadastro realizado com sucesso!\n" + ('-' * 60))

                    while True:
                        try:
                            mod_pesquisa = int(input("\nO QUE DESEJA FAZER AGORA?"
                                                     "\n1 - Voltar ao menu de cadastro"
                                                     "\n2 - Prosseguir para o módulo de pesquisa avançada"
                                                     "\nDIGITE SUA ESCOLHA: "))

                        except BaseException:
                            print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + (
                                    '-' * 60))
                            continue

                        if mod_pesquisa == 1:
                            print(('-' * 60) + "\nVocê será redirecionado ao menu de cadastro! Aguarde...\n" + (
                                    '-' * 60))
                            break

                        elif mod_pesquisa == 2:
                            runpy.run_module(mod_name=Py_03)
                            break

                        else:
                            print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + (
                                    '-' * 60))
                            continue

                elif desqualificado.upper() == "N":
                    print(
                        ('-' * 60) + "\nVocê será redirecionado ao menu de cadastro! Aguarde...\n" + ('-' * 60))
                    break

        elif novo_registro_dec.upper() == "N":
            print(('-' * 60) + "\nVocê será redirecionado ao menu principal! Aguarde...\n" + ('-' * 60))
            break

        else:
            print(('-' * 60) + '\nIsso não parece ser um valor válido! Tente Novamente.\n' + ('-' * 60))
            continue