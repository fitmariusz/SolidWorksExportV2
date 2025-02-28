import os
import re

import pymsgbox


def test_title_line(line_title: list) -> None:
    finish_version = line_title[3 : len(line_title) - 1]
    for i in range(len(finish_version)):
        finish_version[i] = re.sub("<[^>]+>", "", finish_version[i])
        finish_version[i] = re.sub("[" + '"' + "]", "", finish_version[i])
        if finish_version[i].rfind("(") == -1 or finish_version[i].rfind(")") == -1:
            pymsgbox.alert(
                f"Błąd w kolumnie {i+3} \nBrak nawiasu w nazwie wykończenia: {finish_version[i]}",
                "Nieprawidłowe dane.",
                icon=0,
            )
            pymsgbox.alert(
                "Przerwano generowanie plików...", "Uwaga", timeout=2000, icon=0
            )
            os.remove(1)


def test_quantity(table_test: list) -> None:
    for row in table_test:
        if row[-1].replace(",", "").isdigit() == False:
            pymsgbox.alert(
                f"Błędne dane w kolimnie ILOŚĆ:",
                "Nieprawidłowe dane.",
                icon=0,
            )
            pymsgbox.alert(
                "Przerwano generowanie plików...", "Uwaga", timeout=2000, icon=0
            )
            os.remove(1)


def test_index_boms(line_title: list) -> None:
    if len(line_title) != 4:
        lapms_list = line_title[3:-1]
        index_list = list(map(lambda x: x.split("(")[1].split(")")[0], lapms_list))
        unique_index_list = list(set(index_list))
        if len(index_list) != len(unique_index_list):
            pymsgbox.alert(
                f"Błąd w indeksach opraw - powtarzające się indeksy: {index_list}",
                "Nieprawidłowe dane.",
                icon=0,
            )
            pymsgbox.alert(
                "Przerwano generowanie plików...", "Uwaga", timeout=2000, icon=0
            )
            os.remove(1)


def corect_data(table: list) -> None:
    test_title_line(table[0])
    test_index_boms(table[0])
    test_quantity(table[1:])
