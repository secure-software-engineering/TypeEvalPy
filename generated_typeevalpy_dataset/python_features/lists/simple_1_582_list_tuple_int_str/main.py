# Functions are assigned as elements of a list and then called.


def func1():
    return [32, 87, 81]


def func2():
    return (67, 98, 83)


def func3():
    return 91


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'jnrhl'


b = ["Hello"]
b[0] = func4

f = b[0]()
