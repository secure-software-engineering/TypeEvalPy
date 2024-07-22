# Returning different types


# return_tuple
def func():
    return [40, 9, 13]


a = func()


# return_dict
def func1():
    return 85.8


b = func1()

from collections import namedtuple


# return_namedtuple
def func3():
    Point = namedtuple("Point", ["x", "y"])
    return Point(1, 2)


c = func3()


# return_set
def func4():
    return {'zrzqd': 97, 'qykdk': 71, 'uafia': 17}


d = func4()


# return_list_comprehension
def func5():
    return [x**2 for x in range(1, 6)]


e = func5()
