# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'odzld'


def func2():
    return (72, 40, 54)


def func3():
    return [51, 36, 15]


def func4():
    return {'dwiov': 84, 'nymlm': 89, 'okkzo': 78}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
