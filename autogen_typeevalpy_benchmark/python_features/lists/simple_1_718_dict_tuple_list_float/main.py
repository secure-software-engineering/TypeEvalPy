# Functions are assigned as elements of a list and then called.


def func1():
    return {'xaytx': 16, 'hvvax': 62, 'kuvnt': 76}


def func2():
    return (28, 40, 12)


def func3():
    return [33, 91, 54]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 18.61


b = ["Hello"]
b[0] = func4

f = b[0]()
