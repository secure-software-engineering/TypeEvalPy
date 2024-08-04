# Check if tool type coerces integer and string values.


def func1():
    return 3.46


def func2():
    return {'poama': 92, 'akujg': 12, 'jvulh': 55}


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
