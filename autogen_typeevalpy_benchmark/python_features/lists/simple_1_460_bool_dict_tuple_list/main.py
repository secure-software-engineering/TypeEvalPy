# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return {'dwmkr': 10, 'vkoto': 15, 'jwrdf': 91}


def func3():
    return (62, 22, 36)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [45, 49, 95]


b = ["Hello"]
b[0] = func4

f = b[0]()
