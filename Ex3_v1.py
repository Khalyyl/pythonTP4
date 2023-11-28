def multiply_tuple(tuple_of_numbers, n):
    new_tuple = tuple(x * n for x in tuple_of_numbers)
    return new_tuple

tuple_initial = (1, 2, 3, 4)
print("Tuple initial :",tuple_initial)
n = 5

result_tuple = multiply_tuple(tuple_initial, n)
print("Resultat :", result_tuple)
