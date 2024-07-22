# A generator returns a function which is called.


def func():
    return 'dngwo'


class Cls:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration
        self.n += 1
        return func


output_list = [i for i in Cls(1)]
a = output_list[1]()
