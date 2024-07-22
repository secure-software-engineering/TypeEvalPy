# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (19, 4, 41)


def func2():
    return {'xxung': 69, 'frzeo': 79, 'xpcsl': 91}


def func3():
    return 'ywhks'


def func4():
    return 75.72


(a, b), (c, d) = [(func1, func2), (func3, func4)]
