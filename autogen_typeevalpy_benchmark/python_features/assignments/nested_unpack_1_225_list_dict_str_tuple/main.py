# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [47, 31, 84]


def func2():
    return {'aezuj': 36, 'kpntb': 29, 'chvxj': 78}


def func3():
    return 'zlkae'


def func4():
    return (65, 14, 72)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
