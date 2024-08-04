# Functions are assigned as elements of a list and then called.


def func1():
    return {'tiucu': 42, 'mpqem': 89, 'fgkcf': 29}


def func2():
    return (20, 42, 18)


def func3():
    return [55, 7, 6]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 7.78


b = ["Hello"]
b[0] = func4

f = b[0]()
