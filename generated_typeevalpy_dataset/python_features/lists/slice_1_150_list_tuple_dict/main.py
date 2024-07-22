# A new list is created as a slice of another one containing functions.


def func1():
    return [13, 83, 74]


def func2():
    return (22, 44, 14)


def func3():
    return {'fazug': 71, 'mvebm': 99, 'gnjcq': 55}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
