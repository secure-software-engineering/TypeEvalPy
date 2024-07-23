# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'nalpb'


def func2():
    return 76.69


def func3():
    return (24, 96, 95)


def func4():
    return {'qjiqs': 96, 'htbwr': 7, 'cueyq': 25}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
