# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'znvhf': 69, 'etvhj': 100, 'mhgfk': 29}


def func2():
    return [45, 85, 28]


def func3():
    return 'ajwgj'


def func4():
    return 50.63


(a, b), (c, d) = [(func1, func2), (func3, func4)]
