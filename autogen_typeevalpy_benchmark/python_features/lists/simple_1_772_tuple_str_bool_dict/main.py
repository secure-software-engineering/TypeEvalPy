# Functions are assigned as elements of a list and then called.


def func1():
    return (69, 77, 55)


def func2():
    return 'vioio'


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'aasgp': 98, 'bcrbs': 57, 'nkfhc': 36}


b = ["Hello"]
b[0] = func4

f = b[0]()
