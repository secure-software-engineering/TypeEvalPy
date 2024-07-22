# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 35.22


def func2():
    return (12, 83, 43)


def func3():
    return {'gfuvy': 79, 'hnjay': 93, 'pvdpk': 74}


def func4():
    return [99, 96, 33]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
