# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [14, 52, 53]


def func2():
    return 5


def func3():
    return (72, 71, 1)


def func4():
    return {'vuzqx': 92, 'orliv': 85, 'vvitp': 47}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
