# Functions are assigned as elements of a list and then called.


def func1():
    return [76, 86, 45]


def func2():
    return (89, 41, 4)


def func3():
    return {'fewhr': 57, 'ncfpf': 63, 'tfkcg': 84}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'pllrp'


b = ["Hello"]
b[0] = func4

f = b[0]()
