# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'dhvyj': 99, 'jevxf': 75, 'awxab': 80}


def func2():
    return (82, 32, 74)


def func3():
    return [74, 90, 26]


def func4():
    return 28.96


(a, b), (c, d) = [(func1, func2), (func3, func4)]
