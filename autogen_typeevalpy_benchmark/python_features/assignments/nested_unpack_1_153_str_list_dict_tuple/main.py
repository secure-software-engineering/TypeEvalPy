# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'gkldb'


def func2():
    return [92, 9, 23]


def func3():
    return {'fzfne': 75, 'mpyff': 70, 'bqqsw': 23}


def func4():
    return (94, 50, 74)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
