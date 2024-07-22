# Functions are assigned as elements of a list and then called.


def func1():
    return {'hsaqe': 68, 'hxguh': 49, 'xjmwo': 98}


def func2():
    return [81, 85, 84]


def func3():
    return (66, 87, 65)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 79.78


b = ["Hello"]
b[0] = func4

f = b[0]()
