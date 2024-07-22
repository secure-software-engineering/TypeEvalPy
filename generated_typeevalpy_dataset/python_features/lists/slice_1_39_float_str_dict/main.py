# A new list is created as a slice of another one containing functions.


def func1():
    return 48.67


def func2():
    return 'clikw'


def func3():
    return {'daahf': 31, 'qfuta': 84, 'lzlqv': 72}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
