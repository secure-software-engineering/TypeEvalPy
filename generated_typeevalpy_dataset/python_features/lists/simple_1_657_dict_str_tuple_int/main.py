# Functions are assigned as elements of a list and then called.


def func1():
    return {'vtask': 18, 'cetfi': 91, 'ksigl': 39}


def func2():
    return 'hqsug'


def func3():
    return (37, 3, 36)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 93


b = ["Hello"]
b[0] = func4

f = b[0]()
