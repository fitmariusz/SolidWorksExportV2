import csv
from validate_data import corect_data


def loading_csv(path_file: str, file_name: str) -> list:
    table = []
    with open(path_file, newline="") as csv_file:
        spamreader = csv.reader(csv_file, delimiter="\t", quotechar="|")
        for row in spamreader:
            table.append(row[0].split(";"))
    corect_data(table)
    return table
