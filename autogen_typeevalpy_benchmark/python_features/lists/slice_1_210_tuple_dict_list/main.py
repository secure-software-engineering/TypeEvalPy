# A new list is created as a slice of another one containing functions.


def func1():
    return (12, 22, 62)


def func2():
    return {'ujvoo': 59, 'etbpr': 46, 'ixbaq': 44}


def func3():
    return [40, 96, 52]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
