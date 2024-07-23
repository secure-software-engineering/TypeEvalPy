# Functions are assigned as elements of a list and then called.


def func1():
    return 89


def func2():
    return (66, 83, 64)


def func3():
    return 'ypfpu'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [61, 54, 89]


b = ["Hello"]
b[0] = func4

f = b[0]()
