# A new list is created as a slice of another one containing functions.


def func1():
    return {'zhvto': 39, 'bynpc': 41, 'znoox': 43}


def func2():
    return (90, 17, 92)


def func3():
    return [58, 99, 41]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
