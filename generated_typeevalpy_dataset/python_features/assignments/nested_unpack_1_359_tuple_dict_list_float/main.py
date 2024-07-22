# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (98, 47, 81)


def func2():
    return {'aqxqb': 58, 'nngwg': 78, 'uypzt': 20}


def func3():
    return [74, 35, 2]


def func4():
    return 95.89


(a, b), (c, d) = [(func1, func2), (func3, func4)]
