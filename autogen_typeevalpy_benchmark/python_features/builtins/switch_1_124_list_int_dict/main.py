#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [56, 95, 35]:
            return 46
        case 46:
            return [56, 95, 35]
        case _:
            return "default"


a = func([56, 95, 35])
b = func(46)
c = func({'rpzyg': 58, 'gyoha': 48, 'bqfiu': 51})
