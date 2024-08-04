# A new list is created as a slice of another one containing functions.


def func1():
    return {'emyca': 69, 'mlibj': 96, 'varwa': 52}


def func2():
    return False


def func3():
    return 'qebda'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
