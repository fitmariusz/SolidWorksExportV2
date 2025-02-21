def generateBomsToTxt(boms: list, filename: str, directoryPath: str):
    quantityBoms = len(boms[0]) - 4
    for bom in range(quantityBoms):
        filePath = (
            directoryPath
            + filename.split("(")[0]
            + " ("
            + boms[0][3 + bom].split("(")[1]
            + ".txt"
        )
        f = open(filePath, "w", encoding="utf-8")
        for row in boms:
            text = f"{row[0]}\t{row[1]}\t{row[1]}\t{row[3+bom]}\t{row[-1]}\n"
            f.writelines(text)
        f.close
