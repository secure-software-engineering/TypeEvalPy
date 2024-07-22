# A new list is created as a slice of another one containing functions.


def func1():
    return [13, 24, 22]


def func2():
    return {'jclzh': 23, 'foomh': 78, 'xjikw': 100}


def func3():
    return False


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
