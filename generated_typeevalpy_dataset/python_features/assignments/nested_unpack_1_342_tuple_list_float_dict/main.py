# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (30, 91, 32)


def func2():
    return [58, 64, 54]


def func3():
    return 35.59


def func4():
    return {'drpsa': 40, 'cfmxf': 20, 'jkjvl': 82}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
