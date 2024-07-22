# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'zysbb'


def func2():
    return 4.83


def func3():
    return {'txkaj': 19, 'ufhst': 45, 'cagtz': 19}


def func4():
    return (24, 86, 22)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
