# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (27, 41, 98)


def func2():
    return 2.3


def func3():
    return [25, 22, 58]


def func4():
    return {'kdcrs': 91, 'ielep': 21, 'cqssw': 7}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
