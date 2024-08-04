# Functions are assigned as elements of a list and then called.


def func1():
    return [67, 51, 32]


def func2():
    return {'fpimd': 57, 'ccfsp': 22, 'ueqoe': 66}


def func3():
    return (96, 99, 20)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 69


b = ["Hello"]
b[0] = func4

f = b[0]()
