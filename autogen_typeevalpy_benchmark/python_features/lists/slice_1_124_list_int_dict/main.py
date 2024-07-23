# A new list is created as a slice of another one containing functions.


def func1():
    return [18, 17, 47]


def func2():
    return 90


def func3():
    return {'nfein': 23, 'ixhkn': 36, 'xkhrz': 54}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
