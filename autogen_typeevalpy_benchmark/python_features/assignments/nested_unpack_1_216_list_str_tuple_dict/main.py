# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [18, 58, 21]


def func2():
    return 'eyrzt'


def func3():
    return (62, 46, 6)


def func4():
    return {'fmbjb': 36, 'fxjml': 95, 'bzisn': 34}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
