def sort_number(number):
    new_number = number.split()
    int_list = []
    string_list = []
    for x in new_number:
        int_list.append(int(x))
        int_list.sort()

    for y in int_list:
        string_list.append(str(y))
    final = ' '.join(string_list)

    return final


num = (input("Enter numbers you want sorted with space \n"))



print(sort_number(num))
