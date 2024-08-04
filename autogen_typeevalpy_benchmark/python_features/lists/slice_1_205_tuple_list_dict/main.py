# A new list is created as a slice of another one containing functions.


def func1():
    return (12, 45, 85)


def func2():
    return [48, 55, 44]


def func3():
    return {'zuewl': 26, 'oqkgo': 72, 'ugmxf': 31}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
