# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 95


def func2():
    return 88.97


def func3():
    return (18, 82, 79)


def func4():
    return {'zspjy': 32, 'vtjkf': 88, 'hvacq': 98}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
