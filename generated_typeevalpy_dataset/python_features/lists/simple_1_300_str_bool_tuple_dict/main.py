# Functions are assigned as elements of a list and then called.


def func1():
    return 'ksepu'


def func2():
    return False


def func3():
    return (7, 49, 55)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'chefd': 31, 'wryia': 38, 'yuqql': 81}


b = ["Hello"]
b[0] = func4

f = b[0]()
