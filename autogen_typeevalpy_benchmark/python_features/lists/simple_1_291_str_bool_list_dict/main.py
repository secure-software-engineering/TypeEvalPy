# Functions are assigned as elements of a list and then called.


def func1():
    return 'mawuf'


def func2():
    return True


def func3():
    return [87, 70, 87]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'jbzko': 82, 'kxnte': 74, 'jpgzl': 47}


b = ["Hello"]
b[0] = func4

f = b[0]()
