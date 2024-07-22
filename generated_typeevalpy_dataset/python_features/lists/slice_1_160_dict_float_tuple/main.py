# A new list is created as a slice of another one containing functions.


def func1():
    return {'ggrdm': 73, 'blcfg': 98, 'hycfy': 39}


def func2():
    return 65.03


def func3():
    return (98, 73, 71)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
