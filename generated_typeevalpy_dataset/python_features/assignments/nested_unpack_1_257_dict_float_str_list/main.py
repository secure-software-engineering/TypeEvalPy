# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'bdmgh': 32, 'sohim': 82, 'szgsa': 36}


def func2():
    return 17.75


def func3():
    return 'oupjy'


def func4():
    return [76, 70, 6]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
