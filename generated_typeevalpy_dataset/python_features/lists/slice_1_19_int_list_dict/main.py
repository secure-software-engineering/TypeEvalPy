# A new list is created as a slice of another one containing functions.


def func1():
    return 35


def func2():
    return [42, 89, 69]


def func3():
    return {'ocsfj': 65, 'bagzd': 15, 'zzkvm': 67}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
