# Functions are assigned as elements of a list and then called.


def func1():
    return (59, 56, 92)


def func2():
    return 'mgwmy'


def func3():
    return {'bowql': 66, 'dsyzm': 32, 'wajop': 90}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [62, 90, 70]


b = ["Hello"]
b[0] = func4

f = b[0]()
