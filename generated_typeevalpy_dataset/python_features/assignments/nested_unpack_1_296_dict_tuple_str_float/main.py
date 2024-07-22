# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'mrpsx': 26, 'hwbpu': 28, 'jhitu': 50}


def func2():
    return (4, 61, 92)


def func3():
    return 'moesk'


def func4():
    return 54.66


(a, b), (c, d) = [(func1, func2), (func3, func4)]
