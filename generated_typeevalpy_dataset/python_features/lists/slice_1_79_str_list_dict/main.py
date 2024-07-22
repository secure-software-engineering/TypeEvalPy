# A new list is created as a slice of another one containing functions.


def func1():
    return 'uzunt'


def func2():
    return [54, 56, 39]


def func3():
    return {'vhdth': 100, 'ipyqo': 39, 'bfoao': 40}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
