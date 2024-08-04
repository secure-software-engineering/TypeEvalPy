# A new list is created as a slice of another one containing functions.


def func1():
    return {'mdnal': 97, 'bmjlj': 66, 'fbkqs': 16}


def func2():
    return [46, 59, 25]


def func3():
    return 43.31


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
