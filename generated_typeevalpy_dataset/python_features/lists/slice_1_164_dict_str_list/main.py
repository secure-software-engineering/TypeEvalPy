# A new list is created as a slice of another one containing functions.


def func1():
    return {'dftqb': 11, 'icpfu': 22, 'vokuz': 90}


def func2():
    return 'tctxe'


def func3():
    return [49, 100, 5]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
