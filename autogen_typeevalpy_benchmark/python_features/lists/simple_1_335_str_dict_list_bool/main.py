# Functions are assigned as elements of a list and then called.


def func1():
    return 'cmlns'


def func2():
    return {'oksae': 94, 'pjsqb': 20, 'cziba': 45}


def func3():
    return [76, 82, 23]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
