# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'edsdp'


def func2():
    return 79.7


def func3():
    return (93, 98, 62)


def func4():
    return {'oixah': 85, 'gqbwz': 2, 'cvndb': 2}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
