# A new list is created as a slice of another one containing functions.


def func1():
    return {'qqwkp': 62, 'ctrao': 50, 'sfnpj': 40}


def func2():
    return (7, 51, 70)


def func3():
    return 30.89


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
