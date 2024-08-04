# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 30.69


def func2():
    return {'engfw': 58, 'dmbkk': 48, 'nkgic': 12}


def func3():
    return (69, 93, 25)


def func4():
    return 'bjpbb'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
