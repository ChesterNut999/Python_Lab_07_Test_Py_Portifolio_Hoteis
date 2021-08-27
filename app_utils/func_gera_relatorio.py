import csv

def gera_relatorio():
    db_registros_totais = []
    dir_db_hoteis_aprovados = '/home/Maurilio/PycharmProjects/Python_Lab_07_Test_Py_Portifolio_Hoteis/app_resources/' \
                              'db_hoteis_aprovados.csv'
    dir_db_hoteis_reprovados = '/home/Maurilio/PycharmProjects/Python_Lab_07_Test_Py_Portifolio_Hoteis/app_resources/' \
                               'db_hoteis_reprovados.csv'

    '''faz a leitura dos registros das bases de dados'''
    with open(dir_db_hoteis_aprovados, 'r', encoding='UTF-8', newline='') as db_hoteis_aprovados:
        csv_reader = csv.reader(db_hoteis_aprovados, delimiter=',')

        for db_registros in csv_reader:
            db_registros_totais.append(db_registros)

        db_hoteis_aprovados.close()

    with open(dir_db_hoteis_reprovados, 'r', encoding='UTF-8', newline='') as db_hoteis_reprovados:
        csv_reader2 = csv.reader(db_hoteis_reprovados, delimiter=',')

        for db_registros in csv_reader2:
            db_registros_totais.append(db_registros)

        db_hoteis_reprovados.close()

    return db_registros_totais

    # for i in db_registros_totais:
    #     print(i)

# if __name__ == '__main__':
#     gera_lista_db()



