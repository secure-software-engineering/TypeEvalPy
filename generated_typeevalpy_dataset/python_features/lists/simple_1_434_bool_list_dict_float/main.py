# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return [26, 37, 92]


def func3():
    return {'ribaj': 49, 'oaevi': 33, 'qtnyq': 81}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 84.1


b = ["Hello"]
b[0] = func4

f = b[0]()
