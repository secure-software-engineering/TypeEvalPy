# Functions are assigned as elements of a list and then called.


def func1():
    return [36, 93, 42]


def func2():
    return False


def func3():
    return (8, 54, 25)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'quzvo': 65, 'ahdon': 48, 'ebyhg': 49}


b = ["Hello"]
b[0] = func4

f = b[0]()
