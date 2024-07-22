# A new list is created as a slice of another one containing functions.


def func1():
    return (97, 3, 8)


def func2():
    return {'zhygt': 69, 'xnqfo': 19, 'lssrq': 16}


def func3():
    return 88


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
