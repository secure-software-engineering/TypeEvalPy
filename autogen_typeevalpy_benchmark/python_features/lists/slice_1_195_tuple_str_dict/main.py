# A new list is created as a slice of another one containing functions.


def func1():
    return (27, 1, 33)


def func2():
    return 'cajir'


def func3():
    return {'ynkbf': 25, 'luekm': 40, 'qltzu': 44}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
