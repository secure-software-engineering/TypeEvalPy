# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return 'zkchq'


def func3():
    return {'qsota': 56, 'ybgak': 94, 'ypubl': 52}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (9, 3, 44)


b = ["Hello"]
b[0] = func4

f = b[0]()
