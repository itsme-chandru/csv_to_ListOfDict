from csv import DictReader
with open('addresses.csv', 'r') as read_obj:
    dict_reader = DictReader(read_obj)
    print(read_obj)
    list_of_dict = list(dict_reader)
    print(list_of_dict)
    # print(list_of_dict[0])
    # print(list_of_dict[1])
    # print(type(list_of_dict))

