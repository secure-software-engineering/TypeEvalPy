# Functions are assigned as elements of a list and then called.


def func1():
    return 82.57


def func2():
    return {'rklqx': 4, 'aueld': 66, 'tgdyq': 53}


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 27


b = ["Hello"]
b[0] = func4

f = b[0]()
