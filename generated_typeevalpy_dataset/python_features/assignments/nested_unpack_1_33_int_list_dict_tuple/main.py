# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 46


def func2():
    return [26, 61, 97]


def func3():
    return {'whwdd': 1, 'humck': 49, 'ehkpj': 6}


def func4():
    return (22, 86, 27)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
