# Functions are assigned as elements of a list and then called.


def func1():
    return {'pbwba': 68, 'vnlex': 7, 'uymxh': 55}


def func2():
    return 85


def func3():
    return [73, 48, 96]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (41, 9, 78)


b = ["Hello"]
b[0] = func4

f = b[0]()
