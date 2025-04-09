def check_and_add_the_same_elements(table: list) -> list:
    tableTitle = table[0]
    tableToSearch = table[1:]
    elementSums = {}
    dictionary_name_element_for_index = {}
    for row in tableToSearch:
        dictionary_name_element_for_index[row[3]] = row[1:3]
        id = row[0]
        index = row[3]
        quantity = float(
            row[-1].replace(",", ".")
        )  # Assuming mass is always the last element
        # if len(row) == 5:
        #     other = []
        # else:
        other = row[2:-1]  # All elements between name and mass
        if index in elementSums:
            elementSums[index]["quantity"] += quantity
        else:
            elementSums[index] = {
                "quantity": quantity,
                "other": other,
            }
    newTable = [
        [index] + data["other"] + [data["quantity"]]
        for index, data in elementSums.items()
    ]

    for i in range(len(newTable)):
        newTable[i].insert(0, dictionary_name_element_for_index[newTable[i][0]][0])
    id = 1
    for row in newTable:
        row.pop(1)
        row.insert(0, id)
        id += 1
        if row[-1] == int(row[-1]):
            row[-1] = int(row[-1])
    newTable.insert(0, tableTitle)

    return newTable
