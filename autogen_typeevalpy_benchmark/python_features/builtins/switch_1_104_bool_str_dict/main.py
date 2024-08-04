#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 'yzjys'
        case 'yzjys':
            return True
        case _:
            return "default"


a = func(True)
b = func('yzjys')
c = func({'unpau': 63, 'hqpey': 62, 'nsdux': 35})
