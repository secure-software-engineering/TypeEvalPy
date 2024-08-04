# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'ioafo'


def func2():
    return [39, 95, 80]


def func3():
    return {'gjzzu': 43, 'toudy': 1, 'aoqsa': 98}


def func4():
    return 85


(a, b), (c, d) = [(func1, func2), (func3, func4)]
