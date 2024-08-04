# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'hevqw'


def func2():
    return 2


def func3():
    return (63, 18, 25)


def func4():
    return {'vznmr': 59, 'kvmca': 73, 'thhne': 96}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
