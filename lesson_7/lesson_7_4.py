def common_elements() -> set:
    num_1 = range(0, 100, 3)
    lst_1 = list(num_1)

    num_2 = range(0, 100, 5)
    lst_2 = list(num_2)

    set_1 = set(lst_1)
    set_2 = set(lst_2)

    intersection_set = set_1.intersection(set_2)

    return intersection_set

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}