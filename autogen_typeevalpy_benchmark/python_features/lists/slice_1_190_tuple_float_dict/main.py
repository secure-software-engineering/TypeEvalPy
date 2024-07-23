# A new list is created as a slice of another one containing functions.


def func1():
    return (36, 10, 8)


def func2():
    return 79.87


def func3():
    return {'ebuul': 62, 'qfare': 9, 'etzbp': 8}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
