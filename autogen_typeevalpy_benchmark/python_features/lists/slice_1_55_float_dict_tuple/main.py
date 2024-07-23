# A new list is created as a slice of another one containing functions.


def func1():
    return 26.41


def func2():
    return {'wwznp': 98, 'tuaro': 73, 'cvtdz': 96}


def func3():
    return (61, 27, 79)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
