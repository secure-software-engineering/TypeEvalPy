# Functions are assigned as elements of a list and then called.


def func1():
    return 81


def func2():
    return (71, 81, 96)


def func3():
    return [13, 48, 89]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'lrozf': 71, 'gadgl': 26, 'etzug': 47}


b = ["Hello"]
b[0] = func4

f = b[0]()
