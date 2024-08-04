# The update method of dictionaries is used.


def func1():
    return [20, 70, 51]


def func2():
    return 'agayl'


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
