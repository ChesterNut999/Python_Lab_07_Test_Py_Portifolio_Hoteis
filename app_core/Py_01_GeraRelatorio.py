import csv
import runpy
import app_core.Py_02_ConsultaEcadastra as Py_02

print('\n---------- SISTEMA DE PORTIFÓLIO DE HOTÉIS ----------')
print(('-'*60) + "\nMÓDULO RELATÓRIO\n" + ('-'*60))

gera_ralatorio = input('\nPARA GERAR UM RELATÓRIO DOS CADASTROS REGISTRADOS, DIGITE "G"...'
                       '\nPARA CONTINUAR PRESSIONE QUALQUER TECLA...'
                       '\nPRESSIONE UMA TECLA: ')

if gera_ralatorio.upper() == "G":
    with open('../app_resources/db_hoteis_aprovados.csv', 'r', encoding='UTF-8') as db_hoteis:
        reader_db = csv.reader(db_hoteis, delimiter=',')

    with open('../app_resources/relatorio_cadastros.csv', 'r', encoding='UTF-8') as relatorio:
        reader_relatorio = csv.reader(relatorio, delimiter=',')

        for row in reader_db:
            with open('../app_resources/relatorio_cadastros.csv', 'w', newline='', encoding='UTF-8') as relatorio:
                writer = csv.writer(relatorio, delimiter=',')
                writer.writerow(row)

            db_hoteis.close()
            relatorio.close()
            break

        print(('-' * 60) + "\nRelatório de registros gerado com sucesso!\n" + ('-' * 60))

else:
    runpy.run_module(mod_name=Py_02)
