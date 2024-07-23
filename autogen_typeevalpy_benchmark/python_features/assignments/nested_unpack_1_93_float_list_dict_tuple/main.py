# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 19.81


def func2():
    return [46, 85, 44]


def func3():
    return {'uktcc': 100, 'piuko': 81, 'jduos': 14}


def func4():
    return (75, 42, 49)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
