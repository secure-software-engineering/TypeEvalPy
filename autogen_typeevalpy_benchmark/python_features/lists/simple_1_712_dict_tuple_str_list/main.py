# Functions are assigned as elements of a list and then called.


def func1():
    return {'asopg': 14, 'oarup': 43, 'ziuzi': 75}


def func2():
    return (35, 78, 2)


def func3():
    return 'kbyku'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [21, 60, 2]


b = ["Hello"]
b[0] = func4

f = b[0]()
