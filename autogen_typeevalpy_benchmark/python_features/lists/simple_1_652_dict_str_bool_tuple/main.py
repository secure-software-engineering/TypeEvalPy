# Functions are assigned as elements of a list and then called.


def func1():
    return {'dewez': 24, 'vfpry': 64, 'oyvxh': 30}


def func2():
    return 'iecgy'


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (51, 12, 7)


b = ["Hello"]
b[0] = func4

f = b[0]()
