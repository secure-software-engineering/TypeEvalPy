# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return (53, 82, 96)


def func3():
    return 77


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'unrgp': 100, 'cuflc': 74, 'ljqkb': 6}


b = ["Hello"]
b[0] = func4

f = b[0]()
