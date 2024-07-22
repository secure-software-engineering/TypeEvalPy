# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [74, 44, 60]


def func2():
    return {'tikip': 25, 'ypuhi': 93, 'kmnhw': 55}


def func3():
    return 37


def func4():
    return 'hfzau'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
