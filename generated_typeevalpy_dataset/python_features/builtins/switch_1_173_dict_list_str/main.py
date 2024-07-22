#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'ikzvi': 54, 'dfkap': 6, 'bbhhf': 53}:
            return [37, 40, 47]
        case [37, 40, 47]:
            return {'ikzvi': 54, 'dfkap': 6, 'bbhhf': 53}
        case _:
            return "default"


a = func({'ikzvi': 54, 'dfkap': 6, 'bbhhf': 53})
b = func([37, 40, 47])
c = func('mnndc')
