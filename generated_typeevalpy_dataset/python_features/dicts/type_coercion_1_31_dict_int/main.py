# Check if tool type coerces integer and string values.


def func1():
    return {'yqltv': 23, 'nodon': 9, 'pkpxb': 100}


def func2():
    return 54


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
