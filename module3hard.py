data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    sum_ = 0

    for i in args:
        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            for n in i:
                sum_ += calculate_structure_sum(n)
        elif isinstance(i, str):
            sum_ += len(i)
        elif isinstance(i, int):
            sum_ += i
        elif isinstance(i, dict):
            for key, value in i.items():
                sum_ += calculate_structure_sum(key, value)

    return sum_


result = calculate_structure_sum(data_structure)
print(result)
