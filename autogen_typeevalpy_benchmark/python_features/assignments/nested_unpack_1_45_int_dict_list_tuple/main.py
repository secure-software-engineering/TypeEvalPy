# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 4


def func2():
    return {'qyipq': 69, 'qmsqd': 18, 'bazdg': 50}


def func3():
    return [59, 48, 86]


def func4():
    return (96, 90, 70)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
