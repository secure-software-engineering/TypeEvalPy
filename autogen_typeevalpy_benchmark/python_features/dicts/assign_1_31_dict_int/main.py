# A dictionary key is assigned to a function.


def func1():
    return {'edzav': 85, 'ojdgw': 17, 'jbsif': 4}


def func2():
    return 76


d = {"a": func1}

d["a"] = func2

e = d["a"]()
