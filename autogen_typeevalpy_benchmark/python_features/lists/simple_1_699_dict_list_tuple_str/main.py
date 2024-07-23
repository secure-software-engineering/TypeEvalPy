# Functions are assigned as elements of a list and then called.


def func1():
    return {'npgdh': 5, 'peuez': 20, 'evbrr': 65}


def func2():
    return [16, 8, 80]


def func3():
    return (52, 30, 62)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'trway'


b = ["Hello"]
b[0] = func4

f = b[0]()
