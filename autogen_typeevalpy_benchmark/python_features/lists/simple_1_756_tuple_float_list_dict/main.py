# Functions are assigned as elements of a list and then called.


def func1():
    return (14, 70, 18)


def func2():
    return 77.43


def func3():
    return [43, 18, 24]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'wdank': 8, 'vwjko': 28, 'aesyc': 57}


b = ["Hello"]
b[0] = func4

f = b[0]()
