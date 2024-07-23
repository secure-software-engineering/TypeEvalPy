# Functions are assigned as elements of a list and then called.


def func1():
    return [56, 9, 94]


def func2():
    return 21.42


def func3():
    return {'fasap': 19, 'zital': 17, 'uqfwr': 27}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'yytpu'


b = ["Hello"]
b[0] = func4

f = b[0]()
