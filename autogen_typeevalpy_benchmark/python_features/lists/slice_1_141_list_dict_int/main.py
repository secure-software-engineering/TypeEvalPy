# A new list is created as a slice of another one containing functions.


def func1():
    return [50, 61, 35]


def func2():
    return {'ywpla': 40, 'hucus': 74, 'zshgj': 4}


def func3():
    return 70


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
