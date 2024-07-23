#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [86, 94, 9]:
            return {'mmprx': 91, 'jgbek': 95, 'hplgu': 75}
        case {'mmprx': 91, 'jgbek': 95, 'hplgu': 75}:
            return [86, 94, 9]
        case _:
            return "default"


a = func([86, 94, 9])
b = func({'mmprx': 91, 'jgbek': 95, 'hplgu': 75})
c = func('yqwji')
