# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'qhull': 12, 'aauer': 39, 'uodif': 45}


def func2():
    return 22.05


def func3():
    return (38, 22, 74)


def func4():
    return 46


(a, b), (c, d) = [(func1, func2), (func3, func4)]
