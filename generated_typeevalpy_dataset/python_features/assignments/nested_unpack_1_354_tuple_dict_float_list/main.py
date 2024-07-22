# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (49, 79, 44)


def func2():
    return {'ezlkm': 83, 'lawid': 32, 'rtcel': 41}


def func3():
    return 43.16


def func4():
    return [73, 40, 82]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
