# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'vbtjt'


def func2():
    return [69, 82, 1]


def func3():
    return (97, 17, 5)


def func4():
    return {'tqmqg': 53, 'vifqa': 16, 'hjucb': 29}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
