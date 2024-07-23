# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 1


def func2():
    return 43.91


def func3():
    return 'hipjd'


def func4():
    return {'gbxfq': 10, 'bqlpe': 64, 'tcpfv': 80}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
