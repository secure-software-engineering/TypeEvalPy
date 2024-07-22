# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [2, 86, 36]


def func2():
    return 'xuwqu'


def func3():
    return (45, 46, 9)


def func4():
    return {'xonmt': 77, 'rqcno': 69, 'atntm': 71}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
