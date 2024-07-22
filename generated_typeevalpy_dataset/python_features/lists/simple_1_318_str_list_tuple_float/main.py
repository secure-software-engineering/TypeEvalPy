# Functions are assigned as elements of a list and then called.


def func1():
    return 'gvzlj'


def func2():
    return [71, 53, 70]


def func3():
    return (76, 47, 29)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 53.27


b = ["Hello"]
b[0] = func4

f = b[0]()
