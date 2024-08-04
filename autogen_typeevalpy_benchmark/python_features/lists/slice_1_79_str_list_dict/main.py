# A new list is created as a slice of another one containing functions.


def func1():
    return 'jgagw'


def func2():
    return [69, 55, 99]


def func3():
    return {'oylih': 51, 'dauwj': 33, 'limsa': 20}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
