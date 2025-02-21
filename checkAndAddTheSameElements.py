def checkAndAddTheSameElements(table: list):
    tableTitle = table[0]
    tableToSearch = table[1:]
    elementSums = {}
    for row in tableToSearch:
        id = row[0]
        name = row[1]
        quantity = float(
            row[-1].replace(",", ".")
        )  # Assuming mass is always the last element
        other = row[2:-1]  # All elements between name and mass
        if name in elementSums:
            elementSums[name]["quantity"] += quantity
        else:
            elementSums[name] = {
                "quantity": quantity,
                "other": other,
            }

    newTable = [
        [name] + data["other"] + [data["quantity"]]
        for name, data in elementSums.items()
    ]
    id = 1
    for row in newTable:
        row.insert(0, id)
        id += 1
        if row[-1] == int(row[-1]):
            row[-1] = int(row[-1])
    newTable.insert(0, tableTitle)
    return newTable
