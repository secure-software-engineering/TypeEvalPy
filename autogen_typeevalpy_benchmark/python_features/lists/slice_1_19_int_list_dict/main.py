# A new list is created as a slice of another one containing functions.


def func1():
    return 5


def func2():
    return [86, 14, 99]


def func3():
    return {'anube': 33, 'ilspc': 68, 'bxnug': 98}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
