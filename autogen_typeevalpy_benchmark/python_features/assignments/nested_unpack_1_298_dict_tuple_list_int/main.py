# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'xpuqp': 94, 'ezwcw': 55, 'mzpvh': 95}


def func2():
    return (32, 32, 42)


def func3():
    return [56, 75, 29]


def func4():
    return 76


(a, b), (c, d) = [(func1, func2), (func3, func4)]
