# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 67


def func2():
    return (93, 61, 26)


def func3():
    return {'uvwcs': 94, 'ahtry': 70, 'smjwr': 25}


def func4():
    return [33, 48, 62]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
