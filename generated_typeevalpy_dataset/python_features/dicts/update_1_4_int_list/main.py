# The update method of dictionaries is used.


def func1():
    return [42, 69, 66]


def func2():
    return 46


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()