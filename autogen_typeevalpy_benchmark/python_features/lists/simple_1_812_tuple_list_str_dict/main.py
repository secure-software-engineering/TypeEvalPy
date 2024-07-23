# Functions are assigned as elements of a list and then called.


def func1():
    return (78, 81, 4)


def func2():
    return [21, 13, 27]


def func3():
    return 'aeycl'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'wbvgt': 71, 'bxueh': 36, 'raelx': 43}


b = ["Hello"]
b[0] = func4

f = b[0]()
