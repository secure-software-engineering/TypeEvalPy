# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'txjiz'


def func2():
    return [92, 67, 29]


def func3():
    return (41, 83, 67)


def func4():
    return {'mqebb': 40, 'fyrig': 20, 'jjwvy': 90}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
