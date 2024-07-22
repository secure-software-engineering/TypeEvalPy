# Functions are assigned as elements of a list and then called.


def func1():
    return 7.27


def func2():
    return {'omprk': 69, 'tjxko': 12, 'kzfjb': 62}


def func3():
    return [94, 65, 89]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'fjsnb'


b = ["Hello"]
b[0] = func4

f = b[0]()
