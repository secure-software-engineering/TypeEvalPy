# A new list is created as a slice of another one containing functions.


def func1():
    return [91, 86, 11]


def func2():
    return True


def func3():
    return {'pdvzu': 75, 'jlonm': 2, 'jgump': 54}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
