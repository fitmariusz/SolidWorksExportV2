# Version: 2.0.0

import checkAndAddTheSameElements
import generateBoomsToTxt
import deleteCsvFile
import argparse

from loadingCsv import loadingCsv


def parseArguments() -> str:
    parser = argparse.ArgumentParser(
        description="Export boms from one file csv to files txt."
    )
    parser.add_argument("input_file", help="Path to the csv file.")
    pathFile = parser.parse_args().input_file
    directoryPath = pathFile[0 : pathFile.rfind("\\") + 1]
    fileName = pathFile[pathFile.rfind("\\") + 1 :]
    return pathFile, directoryPath, fileName


def main():
    pathFile, directoryPath, fileName = parseArguments()
    table = loadingCsv(pathFile, fileName)
    print(table)


    # checkAndAddTheSameElements()
    # generateBoomsToTxt()
    # deleteCsvFile()


if __name__ == "__main__":
    main()
