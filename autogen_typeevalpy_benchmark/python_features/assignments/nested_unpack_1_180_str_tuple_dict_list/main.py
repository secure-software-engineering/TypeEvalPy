# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'qgsid'


def func2():
    return (50, 65, 76)


def func3():
    return {'hbbyl': 52, 'nnlrd': 3, 'zmtex': 30}


def func4():
    return [29, 94, 17]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
