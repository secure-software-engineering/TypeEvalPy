# Functions are assigned as elements of a list and then called.


def func1():
    return (75, 1, 82)


def func2():
    return 97.66


def func3():
    return 55


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'veswq'


b = ["Hello"]
b[0] = func4

f = b[0]()
