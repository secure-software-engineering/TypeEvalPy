# A new list is created as a slice of another one containing functions.


def func1():
    return {'vflwx': 13, 'ppcmo': 3, 'aipvl': 65}


def func2():
    return 'betzy'


def func3():
    return 22


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
