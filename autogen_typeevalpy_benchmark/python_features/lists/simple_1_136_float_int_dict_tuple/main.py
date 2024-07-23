# Functions are assigned as elements of a list and then called.


def func1():
    return 18.07


def func2():
    return 73


def func3():
    return {'wrwct': 10, 'dfgoi': 65, 'xrlyu': 66}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (30, 31, 72)


b = ["Hello"]
b[0] = func4

f = b[0]()
