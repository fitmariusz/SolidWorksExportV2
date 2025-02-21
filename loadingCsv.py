import csv

from validateData import corectData


def loadingCsv(pathFile: str, filename: str) -> list:
    table = []
    with open(pathFile, newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter="\t", quotechar="|")
        for row in spamreader:
            table.append(row[0].split(";"))
    corectData(table)
    print('ok')
    return table
