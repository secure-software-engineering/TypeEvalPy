# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (91, 85, 62)


def func2():
    return {'lypaz': 42, 'ryitt': 8, 'yofbq': 96}


def func3():
    return 8.0


def func4():
    return [78, 49, 12]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
