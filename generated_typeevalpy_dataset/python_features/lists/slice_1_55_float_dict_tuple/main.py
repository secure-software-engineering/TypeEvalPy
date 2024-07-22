# A new list is created as a slice of another one containing functions.


def func1():
    return 10.59


def func2():
    return {'xarfs': 6, 'cjbcr': 59, 'cernb': 18}


def func3():
    return (96, 87, 45)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
