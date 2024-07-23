# A new list is created as a slice of another one containing functions.


def func1():
    return {'siarq': 47, 'jfbxi': 67, 'akbfe': 55}


def func2():
    return 'lhrmk'


def func3():
    return (55, 29, 42)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
