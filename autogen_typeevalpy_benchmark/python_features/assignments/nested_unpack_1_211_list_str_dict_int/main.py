# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [19, 16, 6]


def func2():
    return 'apnyh'


def func3():
    return {'txikq': 71, 'nefvf': 60, 'euwwy': 83}


def func4():
    return 71


(a, b), (c, d) = [(func1, func2), (func3, func4)]
