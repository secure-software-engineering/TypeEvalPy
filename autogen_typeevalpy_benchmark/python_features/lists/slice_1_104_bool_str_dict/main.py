# A new list is created as a slice of another one containing functions.


def func1():
    return True


def func2():
    return 'lvyvo'


def func3():
    return {'bkwso': 82, 'ogkja': 79, 'ezmde': 35}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
