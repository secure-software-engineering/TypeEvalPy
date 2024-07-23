# A dictionary key is assigned to a function.


def func1():
    return 90


def func2():
    return (84, 65, 6)


d = {"a": func1}

d["a"] = func2

e = d["a"]()
