# Version: 2.0.1
import argparse

from check_and_add_the_same_elements import check_and_add_the_same_elements
from delete_csv_file import delete_csv_file
from generate_boms_to_txt import generate_boms_to_txt
from loading_csv import loading_csv


def parse_arguments() -> str:
    parser = argparse.ArgumentParser(
        description="Export boms from one file csv to files txt."
    )
    parser.add_argument("input_file", help="Path to the csv file.")
    path_file = parser.parse_args().input_file
    directory_path = path_file[0 : path_file.rfind("\\") + 1]
    file_name = path_file[path_file.rfind("\\") + 1 :]
    return path_file, directory_path, file_name


def main():
    path_file, directory_path, file_name = parse_arguments()
    table = loading_csv(path_file, file_name)
    table = check_and_add_the_same_elements(table)
    generate_boms_to_txt(table, file_name, directory_path)
    delete_csv_file(path_file)


if __name__ == "__main__":
    main()
