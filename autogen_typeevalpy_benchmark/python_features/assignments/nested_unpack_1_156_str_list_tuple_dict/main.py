# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'buffk'


def func2():
    return [88, 81, 83]


def func3():
    return (11, 75, 76)


def func4():
    return {'gvabx': 51, 'ldxvi': 64, 'bleov': 4}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
