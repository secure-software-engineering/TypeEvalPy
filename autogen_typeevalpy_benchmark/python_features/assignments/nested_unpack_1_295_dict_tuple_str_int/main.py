# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'spcvh': 81, 'koezz': 85, 'qwznm': 27}


def func2():
    return (36, 7, 25)


def func3():
    return 'cdvxm'


def func4():
    return 21


(a, b), (c, d) = [(func1, func2), (func3, func4)]
