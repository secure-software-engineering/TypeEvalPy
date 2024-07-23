# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 54


def func2():
    return (31, 70, 46)


def func3():
    return 50.55


def func4():
    return {'nviof': 30, 'bxgvb': 23, 'lmeey': 18}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
