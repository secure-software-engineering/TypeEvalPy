# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (77, 88, 53)


def func2():
    return [41, 58, 62]


def func3():
    return {'wdepi': 79, 'hcjkj': 81, 'voaao': 30}


def func4():
    return 90.78


(a, b), (c, d) = [(func1, func2), (func3, func4)]
