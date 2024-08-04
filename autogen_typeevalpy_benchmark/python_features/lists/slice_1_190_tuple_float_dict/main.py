# A new list is created as a slice of another one containing functions.


def func1():
    return (79, 24, 32)


def func2():
    return 15.11


def func3():
    return {'jgmkf': 78, 'stkyu': 32, 'bwexv': 16}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
