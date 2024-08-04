# Functions are assigned as elements of a list and then called.


def func1():
    return 93.97


def func2():
    return {'xdtxl': 15, 'qeowu': 58, 'jerti': 92}


def func3():
    return (32, 58, 20)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
