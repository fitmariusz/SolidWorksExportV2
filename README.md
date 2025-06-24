Start project: 20.02.2025
Write: Mariusz Fit
finish project: 28.02.2025

SolidWorksExport V2.0.2. -SolidWorksExport_V2_0_2.py

This is the second version of the script for generating a boom txt file from a csv file containing several booms. The csv files are generated from documentation in Solidworks. The next script first tests the data and then generates one boom to one file. The files receive SAP and set in the database.

Operation of the application with

1. loading a table with elements from a csv file - loading_csv.py
2. validate data in table - validate_data.py
3. checks the same elements and adds up their values - check_and_add_the_same_elements.py
4. exports boms to txt files - one boom to one file - generate_booms_to_txt.py
5. deletes csv files - delete_csv_file.py
