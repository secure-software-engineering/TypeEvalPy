# Functions are assigned as elements of a list and then called.


def func1():
    return {'xwqit': 57, 'xfbdt': 82, 'iktsu': 67}


def func2():
    return True


def func3():
    return (38, 48, 94)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 82


b = ["Hello"]
b[0] = func4

f = b[0]()
