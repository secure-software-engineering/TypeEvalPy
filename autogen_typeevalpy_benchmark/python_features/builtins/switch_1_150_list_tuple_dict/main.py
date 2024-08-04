#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [91, 96, 69]:
            return (56, 86, 33)
        case (56, 86, 33):
            return [91, 96, 69]
        case _:
            return "default"


a = func([91, 96, 69])
b = func((56, 86, 33))
c = func({'bqyir': 78, 'xsptz': 40, 'uxlgl': 82})
