#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'skcrh': 61, 'wzfrw': 54, 'oodpe': 75}:
            return [9, 18, 83]
        case [9, 18, 83]:
            return {'skcrh': 61, 'wzfrw': 54, 'oodpe': 75}
        case _:
            return "default"


a = func({'skcrh': 61, 'wzfrw': 54, 'oodpe': 75})
b = func([9, 18, 83])
c = func(83.43)
