# A new list is created as a slice of another one containing functions.


def func1():
    return 89


def func2():
    return 'gllbd'


def func3():
    return {'qhtgy': 39, 'jiooz': 48, 'cylej': 75}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
