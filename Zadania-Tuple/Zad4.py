tuple_in_list = ["element", (1, 2, 3), 4.54, True]
print(tuple_in_list)

tuple_is_tuple = tuple(tuple_in_list)
print(tuple_is_tuple)

tuple_is_list_again = list(tuple_is_tuple)
print(tuple_is_list_again)
