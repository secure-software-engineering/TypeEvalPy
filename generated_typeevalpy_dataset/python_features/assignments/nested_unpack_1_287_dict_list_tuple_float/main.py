# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'pvvxz': 100, 'crmrm': 49, 'uajcn': 7}


def func2():
    return [68, 3, 54]


def func3():
    return (35, 34, 18)


def func4():
    return 65.0


(a, b), (c, d) = [(func1, func2), (func3, func4)]
