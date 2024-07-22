# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 69


def func2():
    return [96, 72, 65]


def func3():
    return 33.96


def func4():
    return {'rziwj': 81, 'ddjks': 66, 'tqeii': 20}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
