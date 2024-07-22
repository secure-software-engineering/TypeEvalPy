# Functions are assigned as elements of a list and then called.


def func1():
    return {'qvpyr': 67, 'ehmxt': 79, 'mnhud': 67}


def func2():
    return [54, 25, 34]


def func3():
    return 'pnajh'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (54, 70, 29)


b = ["Hello"]
b[0] = func4

f = b[0]()
