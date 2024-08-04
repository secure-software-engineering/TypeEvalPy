# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'juxiw': 68, 'lydut': 6, 'wyqqb': 41}


def func2():
    return 70


def func3():
    return (73, 20, 42)


def func4():
    return [65, 90, 29]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
