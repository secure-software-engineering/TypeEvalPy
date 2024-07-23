#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'jmkkd': 86, 'xwzum': 76, 'kkydg': 91}:
            return (43, 25, 72)
        case (43, 25, 72):
            return {'jmkkd': 86, 'xwzum': 76, 'kkydg': 91}
        case _:
            return "default"


a = func({'jmkkd': 86, 'xwzum': 76, 'kkydg': 91})
b = func((43, 25, 72))
c = func(3)
