# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'nlhuj': 35, 'inycn': 35, 'jvpqh': 13}


def func2():
    return [33, 84, 75]


def func3():
    return 'kuttp'


def func4():
    return (25, 67, 44)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
