# Functions are assigned as elements of a list and then called.


def func1():
    return (49, 58, 36)


def func2():
    return 'tjcpy'


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'evqky': 87, 'mphkj': 61, 'xlxyo': 62}


b = ["Hello"]
b[0] = func4

f = b[0]()
