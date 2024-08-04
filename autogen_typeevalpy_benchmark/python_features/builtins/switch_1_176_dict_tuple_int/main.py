#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'unucx': 62, 'ishqc': 19, 'zbsoa': 69}:
            return (24, 5, 33)
        case (24, 5, 33):
            return {'unucx': 62, 'ishqc': 19, 'zbsoa': 69}
        case _:
            return "default"


a = func({'unucx': 62, 'ishqc': 19, 'zbsoa': 69})
b = func((24, 5, 33))
c = func(7)
