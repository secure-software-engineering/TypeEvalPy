# A new list is created as a slice of another one containing functions.


def func1():
    return (79, 33, 88)


def func2():
    return {'yhfmt': 36, 'yfzwc': 89, 'ipnzw': 73}


def func3():
    return 'ruvuf'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
