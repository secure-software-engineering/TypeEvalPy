# The update method of dictionaries is used.


def func1():
    return 26.36


def func2():
    return {'dntkk': 47, 'rsozc': 70, 'ysgss': 1}


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
