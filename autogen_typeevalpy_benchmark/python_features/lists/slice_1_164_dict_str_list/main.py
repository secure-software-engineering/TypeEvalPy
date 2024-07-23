# A new list is created as a slice of another one containing functions.


def func1():
    return {'gynni': 50, 'uriwb': 93, 'ofxio': 5}


def func2():
    return 'husfp'


def func3():
    return [84, 23, 74]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
