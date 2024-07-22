# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (28, 80, 76)


def func2():
    return 'gqbea'


def func3():
    return 56


def func4():
    return {'vvbov': 10, 'mjibx': 60, 'tlfmu': 70}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
