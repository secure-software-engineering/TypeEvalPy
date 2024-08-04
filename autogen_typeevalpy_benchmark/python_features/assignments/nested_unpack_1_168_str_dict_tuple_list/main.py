# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'mekqr'


def func2():
    return {'kkwrb': 30, 'mgjiu': 18, 'ivwrz': 39}


def func3():
    return (96, 57, 100)


def func4():
    return [42, 35, 94]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
