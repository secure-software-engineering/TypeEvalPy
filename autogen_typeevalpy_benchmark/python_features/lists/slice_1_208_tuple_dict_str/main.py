# A new list is created as a slice of another one containing functions.


def func1():
    return (69, 94, 37)


def func2():
    return {'prmew': 62, 'anbbw': 67, 'cgrms': 49}


def func3():
    return 'scntj'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
