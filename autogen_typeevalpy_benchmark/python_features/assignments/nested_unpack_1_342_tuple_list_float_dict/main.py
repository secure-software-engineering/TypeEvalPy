# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (77, 16, 99)


def func2():
    return [41, 43, 75]


def func3():
    return 73.99


def func4():
    return {'utyfc': 32, 'fhkwb': 36, 'nscom': 19}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
