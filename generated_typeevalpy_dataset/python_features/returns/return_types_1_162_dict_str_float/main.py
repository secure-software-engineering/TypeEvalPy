# Returning different types


# return_tuple
def func():
    return {'bcxaa': 76, 'nkvwf': 81, 'wujzy': 26}


a = func()


# return_dict
def func1():
    return 'xlhwh'


b = func1()

from collections import namedtuple


# return_namedtuple
def func3():
    Point = namedtuple("Point", ["x", "y"])
    return Point(1, 2)


c = func3()


# return_set
def func4():
    return 63.41


d = func4()


# return_list_comprehension
def func5():
    return [x**2 for x in range(1, 6)]


e = func5()
