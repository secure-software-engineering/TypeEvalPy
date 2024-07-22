# A new list is created as a slice of another one containing functions.


def func1():
    return True


def func2():
    return {'jvlre': 39, 'cpmvk': 83, 'vujim': 48}


def func3():
    return (89, 61, 99)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
