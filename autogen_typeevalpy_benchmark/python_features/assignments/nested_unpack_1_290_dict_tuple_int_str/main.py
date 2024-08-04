# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'hbzqj': 50, 'wivth': 14, 'fozrh': 81}


def func2():
    return (89, 46, 63)


def func3():
    return 11


def func4():
    return 'xleaa'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
