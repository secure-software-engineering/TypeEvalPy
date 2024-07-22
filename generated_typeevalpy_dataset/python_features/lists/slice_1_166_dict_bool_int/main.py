# A new list is created as a slice of another one containing functions.


def func1():
    return {'keftg': 41, 'hdbrv': 8, 'funon': 37}


def func2():
    return False


def func3():
    return 84


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
