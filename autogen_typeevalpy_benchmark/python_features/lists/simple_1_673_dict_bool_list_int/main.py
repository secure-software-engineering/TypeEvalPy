# Functions are assigned as elements of a list and then called.


def func1():
    return {'azfgd': 69, 'kkmiv': 26, 'qvbuc': 70}


def func2():
    return False


def func3():
    return [8, 51, 73]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 52


b = ["Hello"]
b[0] = func4

f = b[0]()
