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


def testQuantity(table: list) -> None:
    table.pop(0)
    for row in table:
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


def corectData(table: list) -> None:
    testTitleLine(table[0])
    testQuantity(table)
