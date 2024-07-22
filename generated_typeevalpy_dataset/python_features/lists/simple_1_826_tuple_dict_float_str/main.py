# Functions are assigned as elements of a list and then called.


def func1():
    return (53, 14, 73)


def func2():
    return {'khksu': 23, 'mtleh': 68, 'tduov': 18}


def func3():
    return 53.83


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'zzlfy'


b = ["Hello"]
b[0] = func4

f = b[0]()
