# Functions are assigned as elements of a list and then called.


def func1():
    return {'qqkou': 87, 'xdvgo': 31, 'ujjhw': 10}


def func2():
    return True


def func3():
    return 39.44


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (89, 95, 15)


b = ["Hello"]
b[0] = func4

f = b[0]()
