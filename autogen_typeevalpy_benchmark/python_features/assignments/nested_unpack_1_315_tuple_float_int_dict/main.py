# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (97, 18, 26)


def func2():
    return 19.41


def func3():
    return 49


def func4():
    return {'hmvhp': 37, 'mtfue': 54, 'hqqdr': 23}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
