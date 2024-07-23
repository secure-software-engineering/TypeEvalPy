# Check if tool type coerces integer and string values.


def func1():
    return (61, 34, 2)


def func2():
    return {'fcwcm': 45, 'kogwc': 96, 'bfyge': 52}


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
