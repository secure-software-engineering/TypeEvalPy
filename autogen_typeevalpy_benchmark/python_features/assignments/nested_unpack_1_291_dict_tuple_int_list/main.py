# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'dzhmk': 46, 'yhoap': 59, 'cuxip': 75}


def func2():
    return (93, 11, 93)


def func3():
    return 29


def func4():
    return [75, 38, 50]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
