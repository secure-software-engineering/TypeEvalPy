# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'ggius'


def func2():
    return [95, 42, 41]


def func3():
    return {'lgydu': 12, 'cclid': 21, 'julmw': 88}


def func4():
    return (39, 91, 90)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
