# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (38, 70, 71)


def func2():
    return {'jsxjp': 88, 'jlset': 69, 'eruqr': 99}


def func3():
    return [4, 16, 30]


def func4():
    return 78


(a, b), (c, d) = [(func1, func2), (func3, func4)]
