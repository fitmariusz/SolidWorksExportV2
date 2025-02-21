def checkAndAddTheSameElements(table: list):
    # listNameElements = []

    # for row in table:
    #     print(row)
    #     listNameElements.append(row[0])
    # serchTheSameElements = list(set(listNameElements))
    # serchTheSameElements.sort()

    # # print("\nI found the same elements\n")
    # # for row in serchTheSameElements:
    # #     print(row)

    # print("\nHow many elements\n")
    # listCount = []
    # for element in serchTheSameElements:
    #     count = serchTheSameElements.count(element)
    #     listCount.append(count)
    #     print("{} repeted           {} times".format(element, count))
    # tableTitle = table[0]
    # tableToSearch = table[1:]
    # elementSums = {}
    # for row in tableToSearch:
    #     name = row[0]
    #     mass = float(row[3])
    #     other = row[1:3]
    #     # quantity = row[1]
    #     # material = row[2]
    #     if name in elementSums:
    #         elementSums[name]["mass"] += mass
    #     else:
    #         elementSums[name] = {
    #             "mass": mass,
    #             "other": other,
    #         }

    # # Create a new table with summed values and no duplicates
    # newTable = [
    #     [name,data["other"] ,data["mass"]]
    #     for name, data in elementSums.items()
    # ]
    # newTable.insert(0, tableTitle)

    # for elements in newTable:
    #     print(elements)
    # for name, data in elementSums.items():
    #     print(
    #         "{} has a total mass of {}, quantity of {}, and material {}".format(
    #             name, data["mass"], data["quantity"], data["material"]
    #         )
    #     )
    tableTitle = table[0]
    tableToSearch = table[1:]
    elementSums = {}
    for row in tableToSearch:
        id = row[0]
        name = row[1]
        quantity = float(row[-1])  # Assuming mass is always the last element
        other = row[2:-1]  # All elements between name and mass
        if name in elementSums:
            elementSums[name]["quantity"] += quantity
        else:
            elementSums[name] = {
                "id": id,
                "quantity": quantity,
                "other": other,
            }

    # Create a new table with summed values and no duplicates
    newTable = [
        data["id"] + [name] + data["other"] + [data["mass"]]
        for name, data in elementSums.items()
    ]
    newTable.insert(0, tableTitle)

    for elements in newTable:
        print(elements)
