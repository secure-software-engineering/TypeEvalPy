# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (72, 85, 82)


def func2():
    return {'ubdfa': 93, 'gslzy': 19, 'bjsmm': 16}


def func3():
    return 35.61


def func4():
    return 27


(a, b), (c, d) = [(func1, func2), (func3, func4)]
