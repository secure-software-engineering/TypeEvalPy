# A dictionary key is assigned to a function.


def func1():
    return 'laxzr'


def func2():
    return (86, 83, 35)


d = {"a": func1}

d["a"] = func2

e = d["a"]()
