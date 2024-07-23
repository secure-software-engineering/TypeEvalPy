# Check if tool type coerces integer and string values.


def func1():
    return {'tbgus': 94, 'fmjbm': 91, 'fynro': 16}


def func2():
    return False


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
