# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 26.96


def func2():
    return [22, 57, 58]


def func3():
    return {'gybvv': 54, 'cwiqt': 54, 'noyqz': 12}


def func4():
    return 'sfpbw'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
