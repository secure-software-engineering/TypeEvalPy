# A new list is created as a slice of another one containing functions.


def func1():
    return {'nbvoy': 32, 'bentm': 17, 'foczh': 44}


def func2():
    return 41.09


def func3():
    return [93, 13, 94]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
