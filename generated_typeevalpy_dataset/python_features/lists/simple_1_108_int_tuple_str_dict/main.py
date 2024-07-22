# Functions are assigned as elements of a list and then called.


def func1():
    return 71


def func2():
    return (88, 52, 81)


def func3():
    return 'wjjoh'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'cmujv': 88, 'wlhvn': 70, 'hrxxa': 45}


b = ["Hello"]
b[0] = func4

f = b[0]()
