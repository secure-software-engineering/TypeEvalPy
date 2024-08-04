# Functions are assigned as elements of a list and then called.


def func1():
    return {'weefh': 17, 'cncov': 60, 'lgobn': 11}


def func2():
    return 65.03


def func3():
    return (96, 14, 100)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [25, 97, 15]


b = ["Hello"]
b[0] = func4

f = b[0]()
