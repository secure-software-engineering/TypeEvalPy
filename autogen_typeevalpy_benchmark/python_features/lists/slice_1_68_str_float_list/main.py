# A new list is created as a slice of another one containing functions.


def func1():
    return 'cnzqy'


def func2():
    return 1.76


def func3():
    return [84, 20, 73]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
