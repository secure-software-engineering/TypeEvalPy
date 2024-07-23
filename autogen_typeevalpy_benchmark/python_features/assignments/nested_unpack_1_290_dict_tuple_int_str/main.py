# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'vwvji': 84, 'fhkoy': 45, 'xjttj': 17}


def func2():
    return (63, 91, 100)


def func3():
    return 14


def func4():
    return 'tkutz'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
