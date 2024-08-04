# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return 83


def func3():
    return {'ultll': 84, 'qkwdg': 72, 'auljg': 36}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (15, 91, 26)


b = ["Hello"]
b[0] = func4

f = b[0]()
