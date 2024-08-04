# The key of a dictionary is passed as a function parameter.


def func1(key="a"):
    return d[key]()


def func2():
    return 'jxjlb'


def func3():
    return {'vufth': 66, 'zlegr': 78, 'bpvne': 15}


d = {"a": func2, "b": func3}

e = func1()
f = func1("b")
