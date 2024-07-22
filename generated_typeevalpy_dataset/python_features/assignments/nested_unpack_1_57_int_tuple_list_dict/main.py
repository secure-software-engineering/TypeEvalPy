# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 31


def func2():
    return (69, 5, 65)


def func3():
    return [78, 81, 14]


def func4():
    return {'wxixv': 26, 'eezpf': 2, 'ntnfm': 83}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
