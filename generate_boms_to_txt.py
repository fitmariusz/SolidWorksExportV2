def generate_boms_to_txt(boms: list, file_name: str, directory_path: str):
    quantity_boms = len(boms[0]) - 4
    for bom in range(quantity_boms):
        file_path = (
            directory_path
            + file_name.split("(")[0]
            + " ("
            + boms[0][3 + bom].split("(")[1]
            + ".txt"
        )
        f = open(file_path, "w", encoding="utf-8")
        for row in boms:
            text = f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3+bom]}\t{row[-1]}\n"
            f.writelines(text)
        f.close
