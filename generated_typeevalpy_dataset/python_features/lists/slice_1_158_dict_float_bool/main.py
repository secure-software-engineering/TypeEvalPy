# A new list is created as a slice of another one containing functions.


def func1():
    return {'bougy': 56, 'tguge': 47, 'rhdbg': 20}


def func2():
    return 62.68


def func3():
    return False


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
