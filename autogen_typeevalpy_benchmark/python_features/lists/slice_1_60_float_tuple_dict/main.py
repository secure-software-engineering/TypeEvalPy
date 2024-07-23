# A new list is created as a slice of another one containing functions.


def func1():
    return 40.47


def func2():
    return (5, 62, 42)


def func3():
    return {'rorbm': 76, 'qvysy': 90, 'jtjnf': 20}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
