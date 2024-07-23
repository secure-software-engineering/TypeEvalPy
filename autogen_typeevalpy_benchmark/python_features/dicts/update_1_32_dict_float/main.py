# The update method of dictionaries is used.


def func1():
    return 31.89


def func2():
    return {'crgxq': 46, 'rbrbq': 65, 'edjcz': 65}


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
