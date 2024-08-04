# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (94, 62, 6)


def func2():
    return 18


def func3():
    return {'rdaqf': 87, 'jipfn': 86, 'utfcw': 12}


def func4():
    return 'zkmpn'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
