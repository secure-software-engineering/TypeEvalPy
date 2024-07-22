# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'zmora': 100, 'hpzoa': 65, 'fsgmk': 38}


def func2():
    return (79, 83, 5)


def func3():
    return [62, 14, 79]


def func4():
    return 'uglnd'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
