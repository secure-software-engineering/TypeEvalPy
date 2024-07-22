# A dictionary key is assigned to a function.


def func1():
    return (69, 100, 85)


def func2():
    return 'cdblg'


d = {"a": func1}

d["a"] = func2

e = d["a"]()
