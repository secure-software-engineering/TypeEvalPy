# Functions are assigned as elements of a list and then called.


def func1():
    return 57


def func2():
    return 51.84


def func3():
    return 'aqzwm'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'jumun': 42, 'jnrwr': 3, 'xyfgf': 92}


b = ["Hello"]
b[0] = func4

f = b[0]()
