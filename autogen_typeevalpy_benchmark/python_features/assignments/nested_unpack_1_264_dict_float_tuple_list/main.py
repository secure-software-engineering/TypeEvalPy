# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'xwciq': 79, 'setcs': 21, 'qcssz': 49}


def func2():
    return 55.48


def func3():
    return (6, 99, 22)


def func4():
    return [43, 73, 85]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
