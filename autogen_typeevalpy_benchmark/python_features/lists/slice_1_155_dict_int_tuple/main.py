# A new list is created as a slice of another one containing functions.


def func1():
    return {'cmafn': 44, 'budlv': 99, 'vopsy': 34}


def func2():
    return 25


def func3():
    return (36, 81, 43)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
