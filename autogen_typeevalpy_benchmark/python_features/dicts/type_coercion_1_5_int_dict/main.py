# Check if tool type coerces integer and string values.


def func1():
    return 16


def func2():
    return {'xnufj': 6, 'gcrst': 85, 'tubxk': 85}


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
