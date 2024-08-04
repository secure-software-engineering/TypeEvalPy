# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'qekme': 57, 'fkzyy': 79, 'frffe': 63}


def func2():
    return 69.1


def func3():
    return [59, 32, 55]


def func4():
    return (52, 100, 6)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
