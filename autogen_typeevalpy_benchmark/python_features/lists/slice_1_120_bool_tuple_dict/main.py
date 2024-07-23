# A new list is created as a slice of another one containing functions.


def func1():
    return True


def func2():
    return (32, 13, 31)


def func3():
    return {'gswlv': 46, 'ezwah': 24, 'rpfvy': 27}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
