# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (36, 22, 47)


def func2():
    return [99, 39, 44]


def func3():
    return 23


def func4():
    return {'oryll': 13, 'hiwfu': 17, 'hsgsr': 25}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
