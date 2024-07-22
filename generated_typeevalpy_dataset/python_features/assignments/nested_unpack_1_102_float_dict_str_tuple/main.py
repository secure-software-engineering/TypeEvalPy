# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 31.62


def func2():
    return {'gzfji': 18, 'qaeoo': 11, 'nwhmo': 79}


def func3():
    return 'uvwhf'


def func4():
    return (53, 69, 6)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
