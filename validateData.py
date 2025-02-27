import os
import re

import pymsgbox


def testTitleLine(lineTitle: list) -> None:
    finishVersion = lineTitle[3 : len(lineTitle) - 1]
    for i in range(len(finishVersion)):
        finishVersion[i] = re.sub("<[^>]+>", "", finishVersion[i])
        finishVersion[i] = re.sub("[" + '"' + "]", "", finishVersion[i])
        if finishVersion[i].rfind("(") == -1 or finishVersion[i].rfind(")") == -1:
            pymsgbox.alert(
                f"Błąd w kolumnie {i+3} \nBrak nawiasu w nazwie wykończenia: {finishVersion[i]}",
                "Nieprawidłowe dane.",
                icon=0,
            )
            pymsgbox.alert(
                "Przerwano generowanie plików...", "Uwaga", timeout=2000, icon=0
            )
            os.remove(1)


def testQuantity(tableTest: list) -> None:
    for row in tableTest:
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
        lapms_list= line_title[3:-1]
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

def corectData(table: list) -> None:
    testTitleLine(table[0])
    test_index_boms(table[0])
    testQuantity(table[1:])
