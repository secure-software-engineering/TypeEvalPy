# A new list is created as a slice of another one containing functions.


def func1():
    return {'fejku': 99, 'hfpsk': 37, 'nqdgc': 61}


def func2():
    return [40, 27, 91]


def func3():
    return (22, 83, 78)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
