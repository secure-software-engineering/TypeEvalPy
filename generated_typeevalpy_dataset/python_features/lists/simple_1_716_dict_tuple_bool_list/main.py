# Functions are assigned as elements of a list and then called.


def func1():
    return {'jaehk': 3, 'dozwd': 64, 'xtspp': 39}


def func2():
    return (78, 66, 17)


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [88, 21, 14]


b = ["Hello"]
b[0] = func4

f = b[0]()
