# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'ttgbt'


def func2():
    return 42.07


def func3():
    return {'fbeqn': 88, 'nltpl': 95, 'gfase': 70}


def func4():
    return [82, 55, 20]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
