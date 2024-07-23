# A new list is created as a slice of another one containing functions.


def func1():
    return 49.79


def func2():
    return {'yxqke': 60, 'pijwp': 78, 'qmsow': 25}


def func3():
    return 49


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
