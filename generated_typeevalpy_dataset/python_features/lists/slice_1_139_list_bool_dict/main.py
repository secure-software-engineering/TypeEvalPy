# A new list is created as a slice of another one containing functions.


def func1():
    return [96, 70, 45]


def func2():
    return True


def func3():
    return {'bckji': 97, 'gghsl': 45, 'ubkwy': 54}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
