# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'fanmc': 10, 'jddpf': 70, 'xsswh': 95}


def func2():
    return 64


def func3():
    return 61.44


def func4():
    return [98, 61, 3]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
