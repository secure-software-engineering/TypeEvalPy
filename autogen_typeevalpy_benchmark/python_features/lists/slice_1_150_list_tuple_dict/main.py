# A new list is created as a slice of another one containing functions.


def func1():
    return [94, 51, 72]


def func2():
    return (23, 36, 29)


def func3():
    return {'qdfab': 84, 'mdtkf': 58, 'iinlv': 23}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
