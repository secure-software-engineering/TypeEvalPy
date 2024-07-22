# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 54


def func2():
    return {'ctwss': 54, 'lbsez': 83, 'juyri': 41}


def func3():
    return (84, 85, 14)


def func4():
    return [97, 29, 28]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
