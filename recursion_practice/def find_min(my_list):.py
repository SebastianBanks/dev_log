def find_min(my_list):
    if len(my_list) == 0:
        return None

    if len(my_list) == 1:
        return my_list

    min = my_list[0] if my_list[0] < my_list[1] else my_list[1]
    my_list[1] = min

    return find_min(my_list[1:])


print(find_min([3, 9, 7, 4, 1]))



