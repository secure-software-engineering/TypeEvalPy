# Functions are assigned as elements of a list and then called.


def func1():
    return 80.77


def func2():
    return False


def func3():
    return 45


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'ssjhf': 64, 'osysr': 51, 'aqxkw': 14}


b = ["Hello"]
b[0] = func4

f = b[0]()
