# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return 'bhfvn'


def func3():
    return {'vlded': 45, 'fnooi': 66, 'ohzeo': 48}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [100, 69, 16]


b = ["Hello"]
b[0] = func4

f = b[0]()
