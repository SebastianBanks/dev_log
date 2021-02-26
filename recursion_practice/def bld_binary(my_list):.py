def bld_binary(my_list):
    if len(my_list) == 0:
        return "No Child"
    else:
        middle_index = len(my_list) // 2
        middle_value = my_list[middle_index]

        tree_node = {"data": middle_value}
        tree_node["left_child"] = bld_binary(my_list[:middle_index])
        tree_node["right_child"] = bld_binary(my_list[middle_index + 1:])
        return tree_node

sorted_list = [12, 13, 14, 15, 16]

binary_search_tree = bld_binary(sorted_list)
print(binary_search_tree)

    