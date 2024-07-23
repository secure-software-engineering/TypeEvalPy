# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [84, 46, 78]


def func2():
    return (87, 12, 57)


def func3():
    return 29.86


def func4():
    return {'rlnad': 17, 'veygf': 15, 'hdjbs': 34}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
