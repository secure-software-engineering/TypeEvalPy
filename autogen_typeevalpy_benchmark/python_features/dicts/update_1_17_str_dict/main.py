# The update method of dictionaries is used.


def func1():
    return {'zfjhf': 50, 'oisjy': 31, 'aeeuw': 36}


def func2():
    return 'sourh'


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
