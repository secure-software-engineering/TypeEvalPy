# A new list is created as a slice of another one containing functions.


def func1():
    return [5, 7, 93]


def func2():
    return (42, 89, 30)


def func3():
    return {'konub': 90, 'ohisy': 11, 'vecmk': 21}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
