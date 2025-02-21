# Version: 2.0.0
import argparse

from checkAndAddTheSameElements import checkAndAddTheSameElements
from generateBomsToTxt import generateBomsToTxt
from loadingCsv import loadingCsv
tableTest = [["name", "quantity", "material", "mass"], ["a", "1", "steel", "1"], ["b", "2", "steel", "2"], ["c", "3", "steel", "3"], ["d", "4", "steel", "4"], ["e", "5", "steel", "5"], ["f", "6", "steel", "6"], ["g", "7", "steel", "7"], ["h", "8", "steel", "8"], ["i", "9", "steel", "9"], ["j", "10", "steel", "10"], ["f", "11", "steel", "11"], ["g", "12", "steel", "12"], ["d", "13", "steel", "13"], ["e", "14", "steel", "14"], ["f", "15", "steel", "15"], ["g", "16", "steel", "16"], ["h", "17", "steel", "17"]]


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
    table = checkAndAddTheSameElements(table)
    generateBomsToTxt(table,fileName, directoryPath)
    




if __name__ == "__main__":
    main()
