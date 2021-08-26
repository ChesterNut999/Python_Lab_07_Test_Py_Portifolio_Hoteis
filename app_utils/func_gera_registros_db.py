import csv

def gera_lista_db():
    '''faz a leitura dos registros das bases de dados'''
    db_registros_totais = []

    with open('../app_resources/db_hoteis_aprovados.csv', 'r', encoding='UTF-8', newline='') as db_hoteis_aprovados:
        csv_reader = csv.reader(db_hoteis_aprovados, delimiter=',')
        csv_reader.__next__()

        for db_registros in csv_reader:
            db_registros_totais.append(db_registros[0])

        db_hoteis_aprovados.close()

    with open('../app_resources/db_hoteis_reprovados.csv', 'r', encoding='UTF-8', newline='') as db_hoteis_reprovados:
        csv_reader2 = csv.reader(db_hoteis_reprovados, delimiter=',')
        csv_reader2.__next__()

        for db_registros in csv_reader2:
            db_registros_totais.append(db_registros[0])

        db_hoteis_reprovados.close()

    return db_registros_totais

    # for i in db_registros_totais:
    #     print(i)

# if __name__ == '__main__':
#     gera_lista_db()



