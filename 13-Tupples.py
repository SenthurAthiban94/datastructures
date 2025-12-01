
def sum_product(input_tuple):
    # TODO
    product = 1
    for i in range(0,len(input_tuple)):
        product *= input_tuple[i]
    return (sum(input_tuple),product)


def tuple_elementwise_sum(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))

def insert_value_front(input_tuple, value_to_insert):
    # TODO
    return (value_to_insert,)+input_tuple

def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)

def get_diagonal(tup):
    # TODO
    return tuple(tup[i][i] for i in range(len(tup)))

def common_elements(tuple1, tuple2):
    # common = tuple()
    # for i in range(len(tuple1)):
    #     if tuple1[i] in tuple2:
    #         common = common+(tuple1[i],)
    # return common
    return tuple(set(tuple1) & set(tuple2))


print(sum_product((1, 2, 3, 4)))
print(tuple_elementwise_sum((1, 2, 3),(4, 5, 6)))
print(insert_value_front((2, 3, 4),1))
print(concatenate_strings(('Hello', 'World', 'from', 'Python')))
print(get_diagonal((
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)))
print(common_elements((1, 2, 3, 4, 5),(4, 5, 6, 7, 8)))