# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (34, 64, 76)


def func2():
    return 'zqjzi'


def func3():
    return [4, 76, 6]


def func4():
    return {'djvpt': 89, 'qjlzk': 9, 'bggic': 40}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
