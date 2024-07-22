# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [29, 27, 20]


def func2():
    return {'cdnqf': 92, 'hpzbl': 25, 'gnhxu': 78}


def func3():
    return (17, 47, 10)


def func4():
    return 'tnvmg'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
