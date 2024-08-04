# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'gkfxb': 35, 'pblfp': 26, 'ejlfj': 43}


def func2():
    return (17, 5, 89)


def func3():
    return 'ohcmk'


def func4():
    return [98, 44, 29]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
