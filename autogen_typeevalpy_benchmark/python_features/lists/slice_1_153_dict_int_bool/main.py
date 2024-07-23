# A new list is created as a slice of another one containing functions.


def func1():
    return {'nijym': 54, 'qgsrh': 65, 'hncpq': 46}


def func2():
    return 12


def func3():
    return False


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
