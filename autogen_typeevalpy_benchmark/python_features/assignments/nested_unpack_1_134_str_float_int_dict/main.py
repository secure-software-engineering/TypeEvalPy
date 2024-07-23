# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'kmoqh'


def func2():
    return 3.66


def func3():
    return 71


def func4():
    return {'umlqg': 39, 'weafi': 90, 'krpfq': 54}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
