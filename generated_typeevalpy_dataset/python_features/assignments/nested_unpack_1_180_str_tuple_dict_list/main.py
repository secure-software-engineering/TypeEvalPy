# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'envdy'


def func2():
    return (83, 18, 11)


def func3():
    return {'yzkrx': 40, 'texgx': 30, 'hwqnt': 30}


def func4():
    return [47, 8, 54]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
