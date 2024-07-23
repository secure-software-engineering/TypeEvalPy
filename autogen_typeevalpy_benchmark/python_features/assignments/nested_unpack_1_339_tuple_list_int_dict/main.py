# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (94, 76, 10)


def func2():
    return [79, 32, 65]


def func3():
    return 88


def func4():
    return {'zbohl': 70, 'bmgys': 77, 'scoyz': 70}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
