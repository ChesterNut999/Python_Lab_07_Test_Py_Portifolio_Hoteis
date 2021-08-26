import csv


def obter_coluna(filename, column):
    with open(filename, encoding='UTF-8', newline='') as bd:
        reader = csv.DictReader(bd, delimiter=',')

        for row in reader:
            yield row[column]