# Check if tool type coerces integer and string values.


def func1():
    return {'vtozn': 94, 'ffwde': 77, 'wojju': 64}


def func2():
    return [43, 30, 44]


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
