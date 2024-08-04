# Check if tool type coerces integer and string values.


def func1():
    return (37, 70, 23)


def func2():
    return {'qwdgd': 90, 'vuodw': 46, 'rwuim': 40}


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
