# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (42, 75, 80)


def func2():
    return 'cpuqq'


def func3():
    return {'dlpfy': 12, 'svquj': 29, 'bofhx': 37}


def func4():
    return 88


(a, b), (c, d) = [(func1, func2), (func3, func4)]
