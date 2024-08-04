# A new list is created as a slice of another one containing functions.


def func1():
    return 2.17


def func2():
    return [33, 35, 40]


def func3():
    return {'yuoor': 94, 'fpgon': 90, 'ksnug': 42}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
