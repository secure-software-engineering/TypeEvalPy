# A new list is created as a slice of another one containing functions.


def func1():
    return 3


def func2():
    return {'nnsbz': 33, 'jvolf': 43, 'hbasy': 92}


def func3():
    return 'hqoih'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
