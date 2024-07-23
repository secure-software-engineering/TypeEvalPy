# A new list is created as a slice of another one containing functions.


def func1():
    return {'vfdsy': 10, 'rivps': 41, 'banai': 51}


def func2():
    return [75, 70, 12]


def func3():
    return 79


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
