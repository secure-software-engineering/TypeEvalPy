# A new list is created as a slice of another one containing functions.


def func1():
    return {'ipbim': 62, 'kdzef': 8, 'aghau': 38}


def func2():
    return 83.64


def func3():
    return [68, 81, 6]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
