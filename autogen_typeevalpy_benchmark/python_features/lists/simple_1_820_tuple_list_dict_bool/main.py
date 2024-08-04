# Functions are assigned as elements of a list and then called.


def func1():
    return (74, 13, 57)


def func2():
    return [84, 89, 79]


def func3():
    return {'zaato': 75, 'zdlba': 90, 'snedx': 57}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
