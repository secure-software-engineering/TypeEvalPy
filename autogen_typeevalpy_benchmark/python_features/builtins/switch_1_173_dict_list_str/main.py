#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'ifuvi': 42, 'ibzsm': 82, 'ydqwt': 77}:
            return [83, 71, 80]
        case [83, 71, 80]:
            return {'ifuvi': 42, 'ibzsm': 82, 'ydqwt': 77}
        case _:
            return "default"


a = func({'ifuvi': 42, 'ibzsm': 82, 'ydqwt': 77})
b = func([83, 71, 80])
c = func('kmxmw')
