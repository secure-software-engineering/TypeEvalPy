# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (47, 89, 87)


def func2():
    return {'zrucd': 69, 'evsea': 25, 'mdgvw': 12}


def func3():
    return [39, 99, 60]


def func4():
    return 15.67


(a, b), (c, d) = [(func1, func2), (func3, func4)]
