# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (55, 3, 15)


def func2():
    return {'edszm': 64, 'wpfov': 95, 'baqsz': 75}


def func3():
    return [77, 94, 71]


def func4():
    return 'zakns'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
