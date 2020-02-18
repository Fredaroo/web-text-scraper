
def import_source():
    print("Enter the path and file name of CSV url list.")
    print("Your csv file must have the following column names: \n"
          "+----------------------------------------------------+ \n"
          "|       uuid (UNIQUE)       |          urls          | \n"
          "+----------------------------------------------------+ \n"
          "[NOTE] The Encoding of the csv should be in UTF-8")
    file_name = input("PAth / file : ")
    return file_name
