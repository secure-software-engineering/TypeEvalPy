# A new list is created as a slice of another one containing functions.


def func1():
    return 75


def func2():
    return [57, 76, 56]


def func3():
    return {'upnjk': 21, 'mtbue': 15, 'rjmbf': 18}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
