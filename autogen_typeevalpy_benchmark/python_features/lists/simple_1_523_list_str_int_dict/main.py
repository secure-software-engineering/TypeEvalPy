# Functions are assigned as elements of a list and then called.


def func1():
    return [93, 11, 90]


def func2():
    return 'iwzqp'


def func3():
    return 18


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'spott': 85, 'grstx': 27, 'wgcax': 4}


b = ["Hello"]
b[0] = func4

f = b[0]()
