# Functions are assigned as elements of a list and then called.


def func1():
    return [66, 16, 99]


def func2():
    return {'jkttj': 67, 'herhl': 21, 'xjofi': 80}


def func3():
    return (76, 20, 35)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 86.64


b = ["Hello"]
b[0] = func4

f = b[0]()
