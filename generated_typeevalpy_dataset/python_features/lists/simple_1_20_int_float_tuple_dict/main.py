# Functions are assigned as elements of a list and then called.


def func1():
    return 46


def func2():
    return 26.96


def func3():
    return (92, 19, 99)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'snxbv': 11, 'gjbbi': 88, 'ffgza': 6}


b = ["Hello"]
b[0] = func4

f = b[0]()
