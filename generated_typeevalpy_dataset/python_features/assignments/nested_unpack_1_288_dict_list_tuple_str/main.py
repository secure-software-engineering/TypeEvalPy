# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'hxnsf': 97, 'khiyd': 3, 'kvugn': 79}


def func2():
    return [28, 81, 10]


def func3():
    return (48, 30, 40)


def func4():
    return 'vmcdh'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
