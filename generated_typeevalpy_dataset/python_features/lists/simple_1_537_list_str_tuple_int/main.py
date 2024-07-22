# Functions are assigned as elements of a list and then called.


def func1():
    return [31, 26, 67]


def func2():
    return 'voyqs'


def func3():
    return (29, 23, 52)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 76


b = ["Hello"]
b[0] = func4

f = b[0]()
