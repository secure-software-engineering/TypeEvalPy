#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'wykod':
            return (95, 86, 59)
        case (95, 86, 59):
            return 'wykod'
        case _:
            return "default"


a = func('wykod')
b = func((95, 86, 59))
c = func({'jjfmf': 33, 'xzjqh': 4, 'uacdx': 60})
