# A new list is created as a slice of another one containing functions.


def func1():
    return 92.9


def func2():
    return {'seasc': 14, 'tnjht': 14, 'hcfdt': 17}


def func3():
    return [22, 27, 10]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
