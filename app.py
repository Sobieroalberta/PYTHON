import csv

path_to_csv_file = 'data.csv'

try:
    string_to_search_for = input(
        "Please search your data using the options listed below:\n(1) - Zip code,\n(2) - State,\n(3) - City,\n(4) - Bank,\n(5) - Type:,\n(6) - Zip code:\n   ")

    file_open = open(path_to_csv_file, 'r')
    data = csv.reader(file_open)

    zipCode, bankName, Type, city, state = [], [], [], [], []

    for i in data:
        zipCode.append(i[5])
        bankName.append(i[1])
        Type.append(i[2])
        city.append(i[3])
        state.append(i[4])

    search = input("Please enter the search term: ")

    if string_to_search_for == '1':
        if search in zipCode:
            print("\nThe zip code " + search + " is found")
        else:
            print("\nThe zip code " + search + " is not found")
    elif string_to_search_for == '2':
        if search in state:
            print("\nThe state " + search + " is found")
        else:
            print("\nThe state " + search + " is not found")
    elif string_to_search_for == '3':
        if search in city:
            print("\nThe city " + search + " is found")
        else:
            print("\nThe city " + search + " is not found")
    elif string_to_search_for == '4':
        if search in bankName:
            print("\nThe bank " + search + " is found")
        else:
            print("\nThe bank " + search + " is not found")
    elif string_to_search_for == '5':
        if search in Type:
            print("\nThe type " + search + " is found")
        else:
            print("\nThe type " + search + " is not found")


    file_open.close()
except Exception as e:
    print(e)