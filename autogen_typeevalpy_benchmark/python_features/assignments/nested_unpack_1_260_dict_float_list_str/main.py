# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'izyht': 79, 'vqtde': 30, 'dazqp': 77}


def func2():
    return 23.99


def func3():
    return [88, 4, 46]


def func4():
    return 'cudvm'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
