# A new list is created as a slice of another one containing functions.


def func1():
    return (31, 89, 78)


def func2():
    return True


def func3():
    return {'svbic': 71, 'xosdf': 53, 'kbmce': 97}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
