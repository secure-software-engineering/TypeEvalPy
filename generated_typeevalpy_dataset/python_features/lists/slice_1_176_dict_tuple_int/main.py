# A new list is created as a slice of another one containing functions.


def func1():
    return {'dgrtr': 84, 'akkqi': 92, 'plymr': 82}


def func2():
    return (62, 55, 90)


def func3():
    return 9


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
