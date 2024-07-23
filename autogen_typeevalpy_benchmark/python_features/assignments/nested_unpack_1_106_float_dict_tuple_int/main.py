# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 8.34


def func2():
    return {'muych': 26, 'fqbkc': 74, 'rtwrc': 98}


def func3():
    return (95, 50, 63)


def func4():
    return 47


(a, b), (c, d) = [(func1, func2), (func3, func4)]
