# Returning different types


# return_tuple
def func():
    return 99


a = func()


# return_dict
def func1():
    return {'vjtez': 68, 'lzbpx': 27, 'vtjuj': 68}


b = func1()

from collections import namedtuple


# return_namedtuple
def func3():
    Point = namedtuple("Point", ["x", "y"])
    return Point(1, 2)


c = func3()


# return_set
def func4():
    return [16, 6, 81]


d = func4()


# return_list_comprehension
def func5():
    return [x**2 for x in range(1, 6)]


e = func5()
