# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 76


def func2():
    return 'gwvcw'


def func3():
    return (32, 97, 60)


def func4():
    return {'orimi': 53, 'mjghp': 63, 'woneg': 72}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
