# The key of a dictionary is passed as a function parameter.


def func1(key="a"):
    return d[key]()


def func2():
    return {'fkzgf': 87, 'upvqa': 1, 'natxz': 14}


def func3():
    return 'oogsm'


d = {"a": func2, "b": func3}

e = func1()
f = func1("b")
