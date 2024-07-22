# A new list is created as a slice of another one containing functions.


def func1():
    return [53, 27, 74]


def func2():
    return {'bbtnt': 35, 'whryb': 87, 'itkpi': 71}


def func3():
    return 'mtkkm'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
