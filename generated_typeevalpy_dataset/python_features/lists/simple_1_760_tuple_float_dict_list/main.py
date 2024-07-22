# Functions are assigned as elements of a list and then called.


def func1():
    return (24, 19, 25)


def func2():
    return 65.15


def func3():
    return {'ilrbq': 80, 'upcqh': 69, 'diryn': 13}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [43, 31, 74]


b = ["Hello"]
b[0] = func4

f = b[0]()
