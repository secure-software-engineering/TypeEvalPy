# A new list is created as a slice of another one containing functions.


def func1():
    return 'xdism'


def func2():
    return {'heqtb': 65, 'hgtdj': 47, 'hrdbi': 46}


def func3():
    return (45, 70, 65)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
