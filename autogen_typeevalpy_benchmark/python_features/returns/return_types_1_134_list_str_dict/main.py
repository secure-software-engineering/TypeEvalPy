# Returning different types


# return_tuple
def func():
    return [30, 61, 66]


a = func()


# return_dict
def func1():
    return 'ycrqz'


b = func1()

from collections import namedtuple


# return_namedtuple
def func3():
    Point = namedtuple("Point", ["x", "y"])
    return Point(1, 2)


c = func3()


# return_set
def func4():
    return {'bpdle': 22, 'njutp': 97, 'mogwn': 24}


d = func4()


# return_list_comprehension
def func5():
    return [x**2 for x in range(1, 6)]


e = func5()
